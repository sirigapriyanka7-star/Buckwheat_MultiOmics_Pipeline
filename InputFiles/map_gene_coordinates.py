# map_gene_coordinates.py
# Maps coordinates from GFF3 to each gene in all_vs_all_NR_best.tsv

import csv

# Input files
blast_file = "all_vs_all_NR_best.tsv"
gff_file   = "non_redundant_genes_final.gff3"

# Output file
output_file = "all_vs_all_NR_with_coords.tsv"

# 1. Load GFF coordinates into a dictionary
gene_coords = {}  # key = gene_id, value = dict of scaffold, start, end, strand

with open(gff_file) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) < 9:
            continue
        scaffold = cols[0]
        feature_type = cols[2]
        start = int(cols[3])
        end = int(cols[4])
        strand = cols[6]
        attributes = cols[8]

        # Extract gene ID from attributes
        gene_id = None
        for attr in attributes.split(";"):
            if attr.startswith("ID="):
                gene_id = attr.replace("ID=", "").strip()
                break
        if gene_id:
            gene_coords[gene_id] = {
                "scaffold": scaffold,
                "start": start,
                "end": end,
                "strand": strand
            }

print(f"Total genes loaded from GFF: {len(gene_coords)}")

# 2. Open BLAST file and map coordinates
with open(blast_file) as infile, open(output_file, "w", newline="") as out:
    writer = csv.writer(out, delimiter="\t")
    
    # Write header
    header = ["Gene1", "Gene2",
              "Gene1_scaffold", "Gene1_start", "Gene1_end", "Gene1_strand",
              "Gene2_scaffold", "Gene2_start", "Gene2_end", "Gene2_strand",
              "Original_line"]
    writer.writerow(header)
    
    missing_genes = set()
    
    for line in infile:
        line = line.strip()
        if not line:
            continue
        cols = line.split("\t")
        gene1 = cols[0]
        gene2 = cols[1]
        
        coord1 = gene_coords.get(gene1)
        coord2 = gene_coords.get(gene2)
        
        if not coord1:
            missing_genes.add(gene1)
        if not coord2:
            missing_genes.add(gene2)
        
        writer.writerow([
            gene1, gene2,
            coord1["scaffold"] if coord1 else "NA",
            coord1["start"] if coord1 else "NA",
            coord1["end"] if coord1 else "NA",
            coord1["strand"] if coord1 else "NA",
            coord2["scaffold"] if coord2 else "NA",
            coord2["start"] if coord2 else "NA",
            coord2["end"] if coord2 else "NA",
            coord2["strand"] if coord2 else "NA",
            line
        ])

print(f"Mapping complete! Output written to {output_file}")
if missing_genes:
    print(f"Warning: {len(missing_genes)} gene(s) not found in GFF")
    print(", ".join(list(missing_genes)[:10]) + ("..." if len(missing_genes) > 10 else ""))