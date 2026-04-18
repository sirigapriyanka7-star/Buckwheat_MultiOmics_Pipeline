# verify_gff3_alignment.py

dup_table_file = "duplication table.txt"
gff3_file = "non_redundant_genes.gff3"

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

# Step 2: Load GFF3 gene positions
gff_genes_pos = {}  # gene_id -> (start, end)
with open(gff3_file) as f:
    for line in f:
        if line.startswith("#"):
            continue
        parts = line.strip().split("\t")
        if parts[2] == "gene":
            gene_id = parts[0]
            start = int(parts[3])
            end = int(parts[4])
            gff_genes_pos[gene_id] = (start, end)

# Step 3: Compare duplication table with GFF3
missing_genes = []
mismatch_genes = []

for gene, (dup_start, dup_end) in dup_genes_pos.items():
    if gene not in gff_genes_pos:
        missing_genes.append(gene)
    else:
        gff_start, gff_end = gff_genes_pos[gene]
        if gff_start != dup_start or gff_end != dup_end:
            mismatch_genes.append((gene, dup_start, dup_end, gff_start, gff_end))

# Step 4: Report
print(f"Total genes in duplication table: {len(dup_genes_pos)}")
print(f"Genes missing in GFF3: {len(missing_genes)}")
if missing_genes:
    print("Missing genes:", missing_genes)

print(f"Genes with start/end mismatch: {len(mismatch_genes)}")
if mismatch_genes:
    print("Mismatches (gene, dup_start, dup_end, gff_start, gff_end):")
    for m in mismatch_genes:
        print(m)

if not missing_genes and not mismatch_genes:
    print("✅ All genes in GFF3 align perfectly with the duplication table!")