#!/bin/bash

# ===============================
# Buckwheat Docking Pipeline
# ===============================

# Create folders
mkdir -p ligands proteins vina_results grids

# -------------------------------
# 1. LIGAND PREPARATION
# -------------------------------

echo "Preparing ligands..."

# Convert MOL2 → PDB
obabel WithaferinA.mol2 -O ligands/WithaferinA.pdb
obabel AlphaCurcumene.mol2 -O ligands/AlphaCurcumene.pdb
obabel Aloesin.mol2 -O ligands/Aloesin.pdb

# Convert PDB → PDBQT (add hydrogens)
obabel ligands/WithaferinA.pdb -O ligands/WithaferinA.pdbqt -xh
obabel ligands/AlphaCurcumene.pdb -O ligands/AlphaCurcumene.pdbqt -xh
obabel ligands/Aloesin.pdb -O ligands/Aloesin.pdbqt -xh


# -------------------------------
# 2. PROTEIN PREPARATION
# -------------------------------

echo "Preparing proteins..."

for i in 1 2 3 4 5; do
    # Convert PDB → PDBQT
    obabel protein${i}.pdb -O proteins/protein${i}.pdbqt -h
done


# -------------------------------
# 3. GRID CALCULATION (BLIND DOCKING)
# -------------------------------

echo "Calculating grid coordinates..."

for i in 1 2 3 4 5; do

    # Convert to XYZ
    obabel protein${i}.pdb -O grids/temp${i}.xyz

    # Extract coordinates
    awk 'NR>2 {print $2, $3, $4}' grids/temp${i}.xyz > grids/coords${i}.txt

    # Get min/max and calculate center & size
    read minx maxx <<< $(awk '{print $1}' grids/coords${i}.txt | sort -n | awk 'NR==1{min=$1} END{print min, $1}')
    read miny maxy <<< $(awk '{print $2}' grids/coords${i}.txt | sort -n | awk 'NR==1{min=$1} END{print min, $1}')
    read minz maxz <<< $(awk '{print $3}' grids/coords${i}.txt | sort -n | awk 'NR==1{min=$1} END{print min, $1}')

    cx=$(echo "($minx+$maxx)/2" | bc -l)
    cy=$(echo "($miny+$maxy)/2" | bc -l)
    cz=$(echo "($minz+$maxz)/2" | bc -l)

    sx=$(echo "($maxx-$minx)+5" | bc -l)
    sy=$(echo "($maxy-$miny)+5" | bc -l)
    sz=$(echo "($maxz-$minz)+5" | bc -l)

    echo "$cx $cy $cz $sx $sy $sz" > grids/grid${i}.txt

done


# -------------------------------
# 4. DOCKING (AutoDock Vina)
# -------------------------------

echo "Running docking..."

ligands=("WithaferinA" "AlphaCurcumene" "Aloesin")

for i in 1 2 3 4 5; do
    read cx cy cz sx sy sz < grids/grid${i}.txt

    for lig in "${ligands[@]}"; do

        vina --receptor proteins/protein${i}.pdbqt \
             --ligand ligands/${lig}.pdbqt \
             --center_x $cx --center_y $cy --center_z $cz \
             --size_x $sx --size_y $sy --size_z $sz \
             --out vina_results/${lig}_protein${i}.pdbqt \
             --log vina_results/${lig}_protein${i}.log \
             --exhaustiveness 8 --num_modes 9 --energy_range 3

    done
done

echo "Docking completed."
