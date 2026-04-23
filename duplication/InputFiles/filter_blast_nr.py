# filter_blast_nr.py

blast_file = "all_vs_all.tsv"
gff_file = "non_redundant_genes_final.gff3"
output_file = "all_vs_all_NR.tsv"

# STEP 1: Extract NR gene IDs from GFF3
nr_genes = set()

with open(gff_file) as gff:
    for line in gff:
        if line.startswith("#"):
            continue
        cols = line.strip().split("\t")
        if len(cols) < 9:
            continue
        feature_type = cols[2]

        # We only take gene entries
        if feature_type == "gene":
            attributes = cols[8]

            # Extract ID=gene_name
            for field in attributes.split(";"):
                if field.startswith("ID="):
                    gene_id = field.replace("ID=", "").strip()
                    nr_genes.add(gene_id)

print("NR gene count:", len(nr_genes))

# STEP 2: Filter BLAST results
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