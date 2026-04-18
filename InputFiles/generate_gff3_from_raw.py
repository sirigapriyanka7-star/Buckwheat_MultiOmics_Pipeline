# generate_gff3_from_raw.py
# Converts gene_positions_raw.txt into a proper non-redundant GFF3 file

input_file = "gene_positions_raw.txt"
output_file = "non_redundant_genes.gff3"

genes = {}

# Step 1: Read the gene positions
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()  # split by whitespace
        if len(parts) < 3:
            continue

        gene_id = parts[0]
        feature = parts[2]  # e.g., CDS, UTR
        try:
            start = int(parts[1])
        except:
            continue

        if feature != "CDS":
            continue  # only keep CDS

        if gene_id not in genes:
            genes[gene_id] = []
        genes[gene_id].append(start)

# Step 2: Write GFF3
with open(output_file, "w") as out:
    out.write("##gff-version 3\n")
    for gene_id, cds_list in genes.items():
        cds_list.sort()
        start = cds_list[0]
        end = cds_list[-1]
        strand = "+"  # default, can change if you have strand info

        # gene line
        out.write(f"{gene_id}\tmanual\tgene\t{start}\t{end}\t.\t{strand}\t.\tID={gene_id}\n")
        # mRNA line
        out.write(f"{gene_id}\tmanual\tmRNA\t{start}\t{end}\t.\t{strand}\t.\tID={gene_id}.t1;Parent={gene_id}\n")
        # CDS lines
        for cds_start in cds_list:
            out.write(f"{gene_id}\tmanual\tCDS\t{cds_start}\t{cds_start+1}\t.\t{strand}\t0\tParent={gene_id}.t1\n")

print(f"GFF3 file created: {output_file}")