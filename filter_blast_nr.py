blast_file = "/mnt/c/GeneDuplicationAnalysis/InputFiles/all_vs_all.tsv"
nr_file = "/mnt/c/GeneDuplicationAnalysis/InputFiles/non_redundant_genes.txt"
output_file = "/mnt/c/GeneDuplicationAnalysis/all_vs_all_NR.tsv"

# Load NR genes
with open(nr_file) as f:
    nr_genes = set(line.strip() for line in f if line.strip())

print("NR gene count:", len(nr_genes))

# Filter BLAST
with open(blast_file) as infile, open(output_file, "w") as out:
    for line in infile:
        cols = line.strip().split("\t")

        if len(cols) < 2:
            continue

        gene1 = cols[0]
        gene2 = cols[1]

        if gene1 in nr_genes and gene2 in nr_genes:
            out.write(line)

print("Filtering complete → all_vs_all_NR.tsv created")
