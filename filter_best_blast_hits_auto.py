# filter_best_blast_hits_auto.py

blast_file = "all_vs_all_NR.tsv"          # Input BLAST table
output_file = "all_vs_all_NR_best.tsv"    # Output cleaned table

# Function to normalize gene IDs
def normalize_gene_id(gene):
    """
    Keep only first 4 segments separated by dots.
    Adjust if your gene IDs have a different unique format.
    """
    parts = gene.split(".")
    return ".".join(parts[:4])

best_hits = {}
header_skipped = False

with open(blast_file) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # skip empty lines or comments

        cols = line.split("\t")
        if len(cols) < 3:
            continue  # must have at least gene1, gene2, score

        gene1 = normalize_gene_id(cols[0])
        gene2 = normalize_gene_id(cols[1])

        # Automatically detect score column: pick the first numeric column after gene2
        score = None
        for col in cols[2:]:
            try:
                score = float(col)
                break
            except ValueError:
                continue
        if score is None:
            continue  # skip if no numeric score found

        pair = tuple(sorted([gene1, gene2]))

        # Keep only the highest score for each gene pair
        if pair not in best_hits or score > best_hits[pair][0]:
            best_hits[pair] = (score,