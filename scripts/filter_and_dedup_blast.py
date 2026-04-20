# filter_and_dedup_blast.py

# Input files
blast_file = "all_vs_all.tsv"
nr_file = "non_redundant_genes_final.gff3"

# Output file
output_file = "all_vs_all_NR_clean.tsv"

# ----------------------------
# Step 1: Load NR genes
# ----------------------------
nr_genes = set()
with open(nr_file) as f:
    for line in f:
        line = line.strip()
        if line:
            # Only take the gene ID (before any whitespace)
            nr_genes.add(line.split()[0])

print(f"Number of NR genes loaded: {len(nr_genes)}")

# ----------------------------
# Step 2: Filter BLAST pairs and remove duplicates
# ----------------------------
written_pairs = set()  # to track already-written gene pairs

with open(blast_file) as infile, open(output_file, "w") as out:
    for line in infile:
        cols = line.strip().split("\t")
        if len(cols) < 2:
            continue
        gene1, gene2 = cols[0], cols[1]

        # Skip if genes are not in NR set
        if gene1 not in nr_genes or gene2 not in nr_genes:
            continue

        # Create a sorted tuple to avoid writing duplicates (geneA-geneB = geneB-geneA)
        pair = tuple(sorted([gene1, gene2]))
        if pair in written_pairs:
            continue

        # Write line and mark pair as written
        out.write(line)
        written_pairs.add(pair)

print(f"Filtering complete! Output file: {output_file}")
print(f"Total unique gene pairs written: {len(written_pairs)}")