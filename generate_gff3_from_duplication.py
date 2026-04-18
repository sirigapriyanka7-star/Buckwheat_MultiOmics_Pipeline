# generate_gff3_from_duplication.py
# Create GFF3 from gene_positions_raw.txt using only genes in duplication table

positions_file = "gene_positions_raw.txt"
dup_table_file = "duplication table.txt"
output_file = "non_redundant_genes.gff3"

# Step 1: Load duplication table gene IDs
dup_genes = set()
with open(dup_table_file) as f:
    next(f)  # skip header
    for line in f:
        line = line.strip()
        if not line:
            continue
        gene1 = line.split()[0]
        gene2 = line.split()[1]
        dup_genes.add(gene1)
        dup_genes.add(gene2)

# Step 2: Read gene positions
genes = {}  # gene_id -> list of (start, end) for CDS
with open(positions_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        gene_id = parts[0]
        start = parts[1]
        end = parts[2]
        feature = parts[3]

        if feature != "CDS":
            continue  # only CDS
        if gene_id not in dup_genes:
            continue  # only genes in duplication table

        try:
            start = int(start)
            end = int(end)
        except:
            continue

        if gene_id not in genes:
            genes[gene_id] = []
        genes[gene_id].append((start, end))

# Step 3: Write GFF3
with open(output_file, "w") as out:
    out.write("##gff-version 3\n")
    for gene_id, cds_list in genes.items():
        cds_list.sort(key=lambda x: x[0])
        gene_start = cds_list[0][0]
        gene_end = cds_list[-1][1]
        strand = "+"  # default; change if you have strand info

        # Gene line
        out.write(f"{gene_id}\tmanual\tgene\t{gene_start}\t{gene_end}\t.\t{strand}\t.\tID={gene_id}\n")
        # mRNA line
        out.write(f"{gene_id}\tmanual\tmRNA\t{gene_start}\t{gene_end}\t.\t{strand}\t.\tID={gene_id}.t1;Parent={gene_id}\n")
        # CDS lines
        for cds_start, cds_end in cds_list:
            out.write(f"{gene_id}\tmanual\tCDS\t{cds_start}\t{cds_end}\t.\t{strand}\t0\tParent={gene_id}.t1\n")

print(f"GFF3 file created: {output_file}")