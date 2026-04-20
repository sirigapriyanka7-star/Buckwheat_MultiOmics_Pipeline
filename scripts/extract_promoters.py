from Bio import SeqIO
import pandas as pd

genome_fasta = "genome.fasta"
dup_file = "dup.tsv"

UPSTREAM = 2000

# LOAD GENOME
genome = {}
for record in SeqIO.parse(genome_fasta, "fasta"):
    genome[record.id.split()[0]] = record.seq

print("Scaffolds loaded:", len(genome))

# LOAD DUP FILE
df = pd.read_csv(dup_file, sep="\t")
print("Rows:", len(df))

promoters = {}

def extract_promoter(seq, start, end, strand):
    if strand == "+":
        s = max(0, start - UPSTREAM)
        return seq[s:start]
    else:
        e = end + UPSTREAM
        return seq[end:e].reverse_complement()

# PROCESS Gene1 + Gene2
for _, row in df.iterrows():

    for gene, scaf, st, en, strd in [
        (row["Gene1"], row["Gene1_scaffold"], row["Gene1_start"], row["Gene1_end"], row["Gene1_strand"]),
        (row["Gene2"], row["Gene2_scaffold"], row["Gene2_start"], row["Gene2_end"], row["Gene2_strand"])
    ]:

        if scaf not in genome:
            continue

        seq = genome[scaf]
        prom = extract_promoter(seq, int(st), int(en), strd)

        promoters[gene] = str(prom)

# SAVE OUTPUT
with open("promoters_final.fasta", "w") as f:
    for i, (g, s) in enumerate(promoters.items()):
        f.write(f">promoter_{i+1}|{g}\n{s}\n")

print("FINAL PROMOTERS:", len(promoters))
