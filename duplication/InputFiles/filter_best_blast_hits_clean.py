# filter_best_blast_hits_clean.py

# Input files
blast_file = "all_vs_all.tsv"  # Your full BLAST table
nr_file = "non_redundant_genes_final.gff3"  # NR gene list

# Output file
output_file = "all_vs_all_NR_best.tsv"

# Step 1: Load NR genes
with open(nr_file) as f:
    nr_genes = set(line.strip().split()[0] for line in f if line.strip())

print(f"Number of NR genes loaded: {len(nr_genes)}")

# Step 2: Helper function to normalize gene IDs
def normalize_gene_id(gene):
    # Keep first 4 segments separated by dots (adjust if needed)
    parts = gene.split(".")
    return ".".join(parts[:4])

# Step 3: Filter and keep best hit per gene pair
best_hits = {}  # key: (gene1_norm, gene2_norm), value: (score, original_line)

with open(blast_file) as infile:
    for line in infile:
        cols = line.strip().split("\t")
        if len(cols) < 3:
            continue
        gene1, gene2, score_str = cols[0], cols[1], cols[2]

        # Skip genes not in NR set
        if gene1 not in nr_genes or gene2 not in nr_genes:
            continue

        try:
            score = float(score_str)
        except ValueError:
            continue

        # Normalize IDs
        gene1_norm = normalize_gene_id(gene1)
        gene2_norm = normalize_gene_id(gene2)
        pair = tuple(sorted([gene1_norm, gene2_norm]))

        # Keep only the highest scoring hit per pair
        if pair not in best_hits or score > best_hits[pair][0]:
            best_hits[pair] = (score, line.strip())

# Step 4: Write output
with open(output_file, "w") as out:
    for _, (, row) in best_hits.items():  # <-- FIXED LINE
        out.write(row + "\n")

print(f"Filtering complete! Output file: {output_file}")
print(f"Total unique gene pairs written: {len(best_hits)}")