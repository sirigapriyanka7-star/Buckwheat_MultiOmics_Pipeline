# classify_duplications.py

import csv
from collections import defaultdict

# Input and output
input_file = "all_vs_all_NR_with_coords_clean.tsv"
output_file = "all_vs_all_NR_duplication_types.tsv"

# Column names (match your file)
gene1_col = "Gene1"
gene2_col = "Gene2"

scaffold1_col = "Gene1_scaffold"
scaffold2_col = "Gene2_scaffold"

start1_col = "Gene1_start"
start2_col = "Gene2_start"

# Step 1: Load gene coordinates and collect genes per scaffold
genes = defaultdict(list)   # genes[scaffold] = list of (geneID, start)
rows = []

with open(input_file) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        rows.append(row)

        g1 = row[gene1_col]
        g2 = row[gene2_col]

        scaf1 = row[scaffold1_col]
        scaf2 = row[scaffold2_col]

        start1 = int(row[start1_col])
        start2 = int(row[start2_col])

        genes[scaf1].append((g1, start1))
        genes[scaf2].append((g2, start2))

# Step 2: Sort genes per scaffold and assign index
gene_index = {}

for scaffold, gene_list in genes.items():
    gene_list = list(set(gene_list))  # remove duplicates
    gene_list.sort(key=lambda x: x[1])  # sort by start position

    for idx, (gene, start) in enumerate(gene_list):
        gene_index[gene] = idx + 1  # 1-based index

# Step 3: Duplication classification function
def classify_duplication(g1, g2, scaffold1, scaffold2):

    # Remove self hits
    if g1 == g2:
        return "Self"

    # Different scaffold → Segmental
    if scaffold1 != scaffold2:
        return "Segmental"

    # Same scaffold → calculate gene distance
    idx1 = gene_index[g1]
    idx2 = gene_index[g2]
    distance = abs(idx1 - idx2)

    if distance == 1:
        return "Tandem"
    elif 2 <= distance <= 5:
        return "Proximal"
    elif distance > 5:
        return "Dispersed"
    else:
        return "Self"

# Step 4: Write output
tandem = proximal = segmental = dispersed = 0

with open(output_file, "w", newline="") as f:
    fieldnames = list(rows[0].keys()) + ["Duplication_Type"]
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()

    for row in rows:
        g1 = row[gene1_col]
        g2 = row[gene2_col]
        s1 = row[scaffold1_col]
        s2 = row[scaffold2_col]

        dup_type = classify_duplication(g1, g2, s1, s2)

        if dup_type == "Self":
            continue

        if dup_type == "Tandem":
            tandem += 1
        elif dup_type == "Proximal":
            proximal += 1
        elif dup_type == "Segmental":
            segmental += 1
        elif dup_type == "Dispersed":
            dispersed += 1

        row["Duplication_Type"] = dup_type
        writer.writerow(row)

# Step 5: Print summary
print("Duplication classification complete!")
print(f"Tandem: {tandem}")
print(f"Proximal: {proximal}")
print(f"Segmental: {segmental}")
print(f"Dispersed: {dispersed}")
print(f"Output file: {output_file}")