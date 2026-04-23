# generate_gff3_aligned.py
# Creates GFF3 aligned with duplication table gene positions

input_positions = "gene_positions_raw.txt"        # your raw gene positions
dup_table_file = "duplication table.txt"         # duplication table
output_file = "non_redundant_genes.gff3"

# Step 0: Load duplication table gene IDs
dup_genes = set()
with open(dup_table_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        gene_id = line.split()[0]  # assuming gene ID is first column
        dup_genes.add(gene_id)

# Step 1: Read gene positions in blocks
genes = {}  # gene_id -> list of (start, end)
with open(input_positions) as f:
    lines = [l.strip() for l in f if l.strip() != ""]
    i = 0
    while i + 3 <= len(lines):
        gene_id = lines[i]
        start_line = lines[i+1]
        end_line = lines[i+2]
        feature_line = lines[i+3]
        i += 4  # move to next block

        if feature_line != "CDS":
            continue  # only CDS

        if gene_id not in dup_genes:
            continue  # skip genes not in duplication table

        try:
            start = int(start_line)
            end = int(end_line)
        except:
            continue  # skip invalid entries

        if gene_id not in genes:
            genes[gene_id] = []
        genes[gene_id].append((start, end))

# Step 2: Write GFF3
with open(output_file, "w") as out:
    out.write("##gff-version 3\n")
    for gene_id, cds_list in genes.items():
        # sort by CDS start
        cds_list.sort(key=lambda x: x[0])
        gene_start = cds_list[0][0]
        gene_end = cds_list[-1][1]
        strand = "+"  # default; change if strand info is available

        # gene line
        out.write(f"{gene_id}\tmanual\tgene\t{gene_start}\t{gene_end}\t.\t{strand}\t.\tID={gene_id}\n")
        # mRNA line
        out.write(f"{gene_id}\tmanual\tmRNA\t{gene_start}\t{gene_end}\t.\t{strand}\t.\tID={gene_id}.t1;Parent={gene_id}\n")
        # CDS lines
        for cds_start, cds_end in cds_list:
            out.write(f"{gene_id}\tmanual\tCDS\t{cds_start}\t{cds_end}\t.\t{strand}\t0\tParent={gene_id}.t1\n")

print(f"GFF3 file created: {output_file}")