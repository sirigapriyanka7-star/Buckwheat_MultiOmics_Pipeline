import pandas as pd
import os

# Create Output folder if not present
os.makedirs("Output", exist_ok=True)

# Read duplication table (tab-separated text with .xlsx name)
dup = pd.read_csv("InputFiles/DuplicationTable.xlsx", sep="\t")

# Read GFF file
gff = pd.read_csv("InputFiles/genes.gff", sep="\t", comment="#", header=None)

gff.columns = [
    "chr", "source", "feature", "start", "end",
    "score", "strand", "phase", "attributes"
]

# Keep only gene features
gff_genes = gff[gff["feature"] == "gene"].copy()

# Extract gene ID from attributes column
gff_genes["gene_id"] = gff_genes["attributes"].str.extract(r'ID=([^;]+)')

# Remove duplicate gene IDs
gff_genes = gff_genes.drop_duplicates(subset="gene_id")

# Merge coordinates for Gene1
dup = dup.merge(
    gff_genes[["gene_id", "chr", "start", "end"]],
    left_on="Gene1",
    right_on="gene_id",
    how="left"
)

dup = dup.rename(columns={
    "chr": "Gene1_chr",
    "start": "Gene1_start",
    "end": "Gene1_end"
})

dup = dup.drop(columns=["gene_id"])

# Merge coordinates for Gene2
dup = dup.merge(
    gff_genes[["gene_id", "chr", "start", "end"]],
    left_on="Gene2",
    right_on="gene_id",
    how="left"
)

dup = dup.rename(columns={
    "chr": "Gene2_chr",
    "start": "Gene2_start",
    "end": "Gene2_end"
})

dup = dup.drop(columns=["gene_id"])

# Save output
dup.to_excel("Output/DuplicationTable_Integrated.xlsx", index=False)

print("Integration completed successfully!")