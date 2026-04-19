#!/bin/bash

echo "=============================="
echo " SYNTENY / COLLINEARITY PIPELINE "
echo "=============================="

# Input files
BLAST="FES_genes.blast"
POS="FES_genes_gff (2).pos"

echo "Step 1: Checking input files..."
ls -lh "$BLAST" "$POS"

echo "Step 2: Filtering BLAST hits..."
python3 filter_best_blast_hits.py \
    --input "$BLAST" \
    --output FES_genes_NR.tsv

echo "Step 3: Preparing gene position file..."
cp "$POS" gene_positions.txt

echo "Step 4: Formatting MCScanX input..."
cat FES_genes_NR.tsv > blast_for_mcscanx.txt

echo "Step 5: Running MCScanX..."
MCScanX synteny_input

echo "Step 6: Listing results..."
ls -lh *.collinearity *.tsv *.txt

echo "DONE ✔"
