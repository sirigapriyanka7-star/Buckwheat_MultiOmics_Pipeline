# filter_blast_with_NR.py

# INPUT FILES
blast_file = "all_vs_all.tsv"
gff_file = "non_redundant_genes_final.gff3"

# OUTPUT FILE
output_file = "all_vs_all_NR_clean.tsv"

# Step 1: Extract gene IDs from GFF3
nr_genes = set()
with open(gff_file) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            # Assuming gene ID is first column; adjust if different
            gene_id = line.split()[0]
            nr_genes.add(gene_id)

print(f"Number of NR genes extracted: {len(nr_genes)}")

# Step 2: Filter BLAST table
filtered_count = 0
with open(blast_file) as infile, open(output_file, "w") as out:
    for line in infile:
        cols = line.strip().split("\t")
        if len(cols) < 2:
            continue
        gene1, gene2 = cols[0], cols[1]
        if gene1 in nr_genes and gene2 in nr_genes:
            out.write(line)
            filtered_count += 1

print(f"Filtering complete. {filtered_count} gene pairs written to {output_file}")