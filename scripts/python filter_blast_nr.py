# Step 1: Filter BLAST using non-redundant genes

nr_file = "non_redundant_genes.txt"
blast_file = "all_vs_all.tsv"
output_file = "all_vs_all_filtered.tsv"

# Load non-redundant genes
nr_genes = set()
with open(nr_file) as f:
    for line in f:
        nr_genes.add(line.strip())

filtered_pairs = set()

with open(blast_file) as f, open(output_file, "w") as out:
    for line in f:
        cols = line.strip().split("\t")
        gene1 = cols[0]
        gene2 = cols[1]

        # Remove self hits
        if gene1 == gene2:
            continue

        # Keep only NR genes
        if gene1 not in nr_genes or gene2 not in nr_genes:
            continue

        # Remove reciprocal duplicates
        pair = tuple(sorted([gene1, gene2]))
        if pair in filtered_pairs:
            continue

        filtered_pairs.add(pair)
        out.write(line)

print("BLAST filtering completed ✔")