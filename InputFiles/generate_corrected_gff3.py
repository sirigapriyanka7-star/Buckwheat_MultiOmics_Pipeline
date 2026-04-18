# generate_corrected_gff3.py
# One-step script to generate GFF3 aligned with duplication table

positions_file = "gene_positions_raw.txt"
dup_table_file = "duplication table.txt"
output_file = "non_redundant_genes_final.gff3"

# Step 1: Load duplication table gene positions
dup_genes_pos = {}  # gene_id -> (start, end)
with open(dup_table_file) as f:
    next(f)  # skip header
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        gene1 = parts[0]
        gene2 = parts[1]
        start1 = int(parts[5])
        end1 = int(parts[6])
        start2 = int(parts[8])
        end2 = int(parts[9])
        dup_genes_pos[gene1] = (start1, end1)
        dup_genes_pos[gene2] = (start2, end2)

# Step 2: Read gene positions and collect CDS
genes = {}  # gene_id -> list of (CDS_start, CDS_end)
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
        if gene_id not in dup_genes_pos:
            continue  # only genes in duplication table

        try:
            start = int(start)
            end = int(end)
        except:
            continue

        if gene_id not in genes:
            genes[gene_id] = []
        genes[gene_id].append((start, end))

# Step 3: Write final corrected GFF3
with open(output_file, "w") as out:
    out.write("##gff-version 3\n")
    for gene_id, cds_list in genes.items():
        # Sort CDS by start
        cds_list.sort(key=lambda x: x[0])
        # Use duplication table positions for gene/mRNA
        gene_start, gene_end = dup_genes_pos[gene_id]
        strand = "+"  # default; change if known

        # Gene line
        out.write(f"{gene_id}\tmanual\tgene\t{gene_start}\t{gene_end}\t.\t{strand}\t.\tID={gene_id}\n")
        # mRNA line
        out.write(f"{gene_id}\tmanual\tmRNA\t{gene_start}\t{gene_end}\t.\t{strand}\t.\tID={gene_id}.t1;Parent={gene_id}\n")
        # CDS lines (trimmed to gene boundaries from duplication table)
        for cds_start, cds_end in cds_list:
            cds_start = max(cds_start, gene_start)
            cds_end = min(cds_end, gene_end)
            out.write(f"{gene_id}\tmanual\tCDS\t{cds_start}\t{cds_end}\t.\t{strand}\t0\tParent={gene_id}.t1\n")

print(f"✅ Final GFF3 created: {output_file}")