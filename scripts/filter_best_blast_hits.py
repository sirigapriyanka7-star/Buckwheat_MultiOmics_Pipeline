# filter_best_blast_hits.py

import csv

# Input BLAST table (already filtered for NR genes)
blast_file = "all_vs_all_NR.tsv"

# Output cleaned BLAST table
output_file = "all_vs_all_NR_best.tsv"

# Dictionary to store best score per gene pair
best_hits = {}

with open(blast_file, "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if len(row) < 3:
            continue  # skip incomplete lines

        gene1 = row[0].strip()
        gene2 = row[1].strip()
        
        try:
            score = float(row[2])  # assuming 3rd column is percent identity / score
        except ValueError:
            continue  # skip if score not numeric

        # Sort gene names to treat pairs symmetrically
        pair = tuple(sorted([gene1, gene2]))

        # Keep the hit if it has higher score than previous
        if pair not in best_hits or score > best_hits[pair][2]:
            best_hits[pair]