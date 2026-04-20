# correct_gff3_positions.py
# Corrects gene positions in GFF3 to exactly match duplication table

dup_table_file = "duplication table.txt"
gff3_file = "non_redundant_genes.gff3"
corrected_gff3 = "non_redundant_genes_corrected.gff3"

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

# Step 2: Read original GFF3
gff_lines = []
with open(gff3_file) as f:
    for line in f:
        gff_lines.append(line.rstrip())

# Step 3: Correct gene/mRNA/CDS positions
corrected_lines = ["##gff-version 3"]
current_gene = None
for line in gff_lines:
    if line.startswith("#"):
        continue
    parts = line.split("\t")
    gene_id = parts[0]
    feature = parts[2]

    if gene_id in dup_genes_pos:
        dup_start, dup_end = dup_genes_pos[gene_id]

        if feature == "gene" or feature == "mRNA":
            parts[3] = str(dup_start)
            parts[4] = str(dup_end)
        elif feature == "CDS":
            # Ensure CDS start/end within corrected gene boundaries
            cds_start = max(int(parts[3]), dup_start)
            cds_end = min(int(parts[4]), dup_end)
            parts[3] = str(cds_start)
            parts[4] = str(cds_end)

        corrected_lines.append("\t".join(parts))

# Step 4: Write corrected GFF3
with open(corrected_gff3, "w") as out:
    for l in corrected_lines:
        out.write(l + "\n")

print(f"✅ Corrected GFF3 created: {corrected_gff3}")