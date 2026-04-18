# filter_best_blast_hits_final.py

blast_file = "all_vs_all_NR.tsv"          # Input BLAST table
output_file = "all_vs_all_NR_best.tsv"    # Output cleaned table

# Function to normalize gene IDs
def normalize_gene_id(gene):
    """
    Keep only first 4 segments separated by dots.
    Adjust if your gene IDs have a different unique format.
    """
    parts = gene.split(".")
    return ".".join(parts[:4])

best_hits = {}

with open(blast_file) as f:
    for line in f:
        cols = line.strip().split("\t")
        if len(cols) < 12:  # Adjust if your BLAST TSV has more/fewer columns
            continue
        gene1 = normalize_gene_id(cols[0])
        gene2 = normalize_gene_id(cols[1])
        score = float(cols[11])  # Assuming bit-score is column 12 (0-index 11). Adjust if needed.
        
        pair = tuple(sorted([gene1, gene2]))
        
        # Keep only the highest score for each pair
        if pair not in best_hits or score > best_hits[pair][0]:
            best_hits[pair] = (score, line.strip())

# Write cleaned BLAST hits
with open(output_file, "w") as out:
    for pair in best_hits:
        out.write(best_hits[pair][1] + "\n")

print(f"Total unique gene pairs written: {len(best_hits)}")
print(f"Output file created: {output_file}")