🧬 Gene Duplication Analysis Pipeline (Windows-Based Python Workflow)

This folder contains a complete and reproducible pipeline for gene duplication analysis of a target gene family (e.g., CBL and CIPK) using BLASTP, genome annotation mapping, and duplication classification.

The workflow was implemented using a Windows-compatible Python environment along with NCBI BLAST+ tools.


---

📌 Overview

This pipeline identifies and classifies gene duplication events by combining:

Protein sequence similarity (BLASTP)

Genome annotation mapping (GFF)

Genomic coordinate analysis

Duplication type classification


The final output provides categorized gene duplication events across the genome.


---

🧬 Input Data

Protein FASTA sequences (gene family dataset)

Genome annotation file (.gff / .gff3)

BLAST database generated from protein sequences



---

⚙️ Workflow Steps

1. Environment Setup

Windows-compatible Python 3.x environment configured

BLAST+ tools installed and verified via Command Prompt

No external Python libraries required (standard libraries used)



---

2. All-vs-All BLASTP Analysis

BLASTP used to detect homologous gene pairs

E-value threshold: 1e-5

Output format: tabular (outfmt 6)

Self-hits retained initially and removed later during filtering



---

3. Non-Redundant Filtering

Custom Python scripts used to:

Remove duplicate gene pairs

Retain best-scoring alignments

Eliminate reciprocal redundancy (A–B vs B–A)



Output: all_vs_all_NR_best.tsv


---

4. Gene Coordinate Mapping

GFF annotation used to map genomic positions

Each gene pair annotated with:

Scaffold ID

Start position

End position

Strand information



Output: all_vs_all_NR_with_coords.tsv


---

5. Data Cleaning & Standardization

Removed malformed entries

Standardized gene IDs and column formats


Output: all_vs_all_NR_with_coords_clean.tsv


---

6. Gene Index Assignment

Genes sorted by scaffold and genomic position

Sequential index assigned per scaffold for distance calculation



---

7. Duplication Distance Calculation

Distance defined as:

| Index(Gene1) − Index(Gene2) |


Used to classify proximity of duplicated genes.


---

8. Duplication Classification

Type	Criteria

Tandem	Distance = 1 (same scaffold)
Proximal	Distance = 2–5
Dispersed	Distance > 5
Segmental	Genes located on different scaffolds



---

📊 Key Results

Total gene duplication pairs identified: 31


Duplication Type	Count

Tandem	0
Proximal	0
Segmental	31
Dispersed	0



---

📁 Output Files

all_vs_all.tsv

all_vs_all_NR.tsv

all_vs_all_NR_best.tsv

all_vs_all_NR_with_coords.tsv

all_vs_all_NR_with_coords_clean.tsv

all_vs_all_NR_duplication_types.tsv

DuplicationTable.xlsx

duplication table.txt



---

🧪 Scripts Used

filter_best_blast_hits_final.py

map_gene_coordinates.py

classify_duplications.py

clean_mapped_table.py

filter_and_dedup_blast.py

generate_gff3_from_duplication.py

verify_gff3_alignment.py



---

📌 Reproducibility

All steps are fully reproducible using modular Python scripts and BLAST command-line tools. Each step generates intermediate outputs that can be independently verified.


---

📊 Summary

This pipeline successfully identified gene duplication events in the target gene family, revealing predominantly segmental duplication patterns, suggesting large-scale genomic duplication rather than tandem expansion.