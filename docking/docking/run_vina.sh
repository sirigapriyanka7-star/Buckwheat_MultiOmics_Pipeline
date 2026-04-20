#!/bin/bash

# =========================
# Buckwheat Docking Script
# Excluding protein 5 due to file issues
# =========================

# List of proteins (final cleaned PDBQT files)
proteins=("protein1_cleaned.pdbqt" "protein2_cleaned.pdbqt" "protein3_cleaned.pdbqt" "protein4_cleaned.pdbqt")

# List of ligands
ligands=("WithaferinA.pdbqt" "AlphaCurcumene.pdbqt" "Aloesin.pdbqt")

# Create output folder
mkdir -p vina_results

# Loop over proteins and ligands
for protein in "${proteins[@]}"; do
    for ligand in "${ligands[@]}"; do

        # Extract protein number from filename
        prot_num=$(echo $protein | grep -oP '\d+')

        # Grid settings for each protein
        if [ "$prot_num" == "1" ]; then
            center_x=7.1405; center_y=-5.406; center_z=-4.1565
            size_x=62.156; size_y=50.812; size_z=59.375
        elif [ "$prot_num" == "2" ]; then
            center_x=0.6095; center_y=-0.8125; center_z=-2.664
            size_x=56.375; size_y=41.875; size_z=44.328
        elif [ "$prot_num" == "3" ]; then
            center_x=-11.0625; center_y=-0.469; center_z=-5.766
            size_x=106.375; size_y=119.062; size_z=88.75
        elif [ "$prot_num" == "4" ]; then
            center_x=-8.5785; center_y=-0.1095; center_z=5.687
            size_x=80.281; size_y=87.657; size_z=75.031
        fi

        # Output file name
        out_file="vina_results/${ligand%.pdbqt}_${protein%.pdbqt}_vina_out.pdbqt"

        # Run AutoDock Vina
        vina --receptor "$protein" --ligand "$ligand" \
             --center_x $center_x --center_y $center_y --center_z $center_z \
             --size_x $size_x --size_y $size_y --size_z $size_z \
             --out "$out_file" --log "${out_file%.pdbqt}.log" \
             --exhaustiveness 8 --num_modes 9 --energy_range 3

    done
done
