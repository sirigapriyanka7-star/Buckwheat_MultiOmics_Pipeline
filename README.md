# 🧬 Buckwheat Multi-Omics Pipeline

![Bioinformatics](https://img.shields.io/badge/Bioinformatics-MultiOmics-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Language](https://img.shields.io/badge/Language-Python%20%7C%20R-orange)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20WSL-lightgrey)
![GPU](https://img.shields.io/badge/GPU-Colab%20Used-yellow)
![License](https://img.shields.io/badge/License-Academic-blue)

---

This repository contains a comprehensive multi-omics analysis pipeline for studying stress-responsive gene families in buckwheat.

> *Note:* Genome-wide and functional analyses were performed on Fagopyrum esculentum, while RNA-seq (transcriptomic) analysis was conducted using Fagopyrum tataricum.

---

## 📌 Project Overview

This project integrates genomics, transcriptomics, and structural biology approaches to identify and characterize stress-responsive gene families and their regulatory mechanisms in buckwheat.

---

## 🎯 Objectives

- Identify stress-responsive gene families (CBL, CIPK, SOS pathway)
- Validate protein function using conserved domains
- Analyze gene structure and chromosomal distribution
- Investigate gene duplication and evolutionary relationships
- Predict and validate protein structures
- Perform molecular docking analysis
- Analyze promoter regions and cis-regulatory elements
- Identify differentially expressed genes under drought stress

---

## 📂 Project Modules

---

## 🧬 Part I: Fagopyrum esculentum (Genome-wide Analysis)

### 🔹 SOS Pathway Analysis
- Identification of SOS pathway components (SOS1, SOS2, SOS3)
- Literature-supported biological interpretation

---

### 🔹 Domain Validation (CBL & CIPK)
- Tool: InterProScan
- CBL → EF-hand calcium-binding domains
- CIPK → Kinase + NAF/FISL domains

✔ Confirms accurate classification of gene families

---

### 🔹 Redundancy Removal & Phylogenetic Analysis
- BLASTp-based identification
- Removal of redundant mappings
- Phylogenetic analysis using MUSCLE

✔ Generated non-redundant gene set

---

### 🔹 Gene Structure Analysis
- Tool: GSDS 2.0
- Input: GFF3 annotation

📊 Findings:
- CBL genes show conserved exon structure
- CIPK genes show high structural variation

---

### 🔹 Chromosomal Mapping
- Tool: MG2C

✔ Revealed gene distribution patterns and clustering

---

### 🔹 Gene Duplication Analysis
- BLASTP + Python workflow

| Type | Count |
|------|------|
| Tandem | 0 |
| Proximal | 0 |
| Segmental | 31 |
| Dispersed | 0 |

✔ Indicates dominance of *segmental duplication*

---

### 🔹 Collinearity & Synteny Analysis
- Tool: MCScanX (WSL environment)

📌 Result:
- No collinear blocks detected
✔ Interpreted as dataset-size limitation

---

### 🔹 Promoter & Cis-Element Analysis
- ~2000 bp upstream promoter regions
- Tool: PLACE database

📊 Key observations:
- Hormone-responsive motifs (ABA, auxin, GA)
- Stress-responsive and light-regulated elements
- Dense regulatory motif architecture

---

### 🔹 Protein Structure Prediction
- Tool: AlphaFold2 (ColabFold, GPU-enabled)

✔ High-confidence 3D structures predicted

---

### 🔹 Structure Validation
- Tools: PROCHECK, ERRAT

✔ Structures show acceptable stereochemical quality

---

### 🔹 Molecular Docking

#### Phytochemicals:
- Withaferin A
- Alpha-Curcumene
- Aloesin

| Protein | Binding Energy | Interpretation |
|--------|----------------|----------------|
| P1 | -7.98 | Strong |
| P3 | -6.18 | Moderate |
| P5 | -6.12 | Moderate |
| P2 | -4.49 | Weak |
| P4 | +11.14 | Discarded |

✔ *P1 identified as top candidate*

---

## 🧬 Part II: RNA-seq Analysis (Fagopyrum tataricum)

---

### 📊 Dataset

*Drought:*
- SRR29434873
- SRR29434877

*Control:*
- SRR29434880
- SRR29434881

---

### ⚙️ Workflow

1. FastQC → Quality control  
2. HISAT2 → Read alignment  
3. SAMtools → BAM processing  
4. featureCounts → Gene quantification  
5. DESeq2 → Differential expression  
6. Visualization → Volcano plot + heatmap  

---

### 📊 Key Findings

- Strong differential gene expression observed
- Clear separation between drought and control samples
- Large number of significantly differentially expressed genes
- Both upregulated and downregulated gene sets identified

✔ Indicates a *strong transcriptomic response to drought stress*

---

### 📁 Output Files

- DEG_results.csv
- significant_DEGs.csv
- upregulated_genes.csv
- downregulated_genes.csv
- volcano_plot.pdf
- heatmap.png

---

## 🧰 Tools & Software Used

### 🔹 Bioinformatics Tools
- HISAT2
- SAMtools
- featureCounts
- FastQC
- BLAST+
- InterProScan
- MUSCLE
- MCScanX
- MG2C
- GSDS 2.0

---

### 🔹 Structural & Docking Tools
- AlphaFold2 (ColabFold)
- PROCHECK
- ERRAT
- AutoDock Vina
- SwissDock
- Open Babel

---

### 🔹 Programming
- Python 3.x
- R

### 🔹 R Packages
- DESeq2
- ggplot2
- pheatmap

---

### 🔹 Environment
- Windows + WSL (Ubuntu)
- Google Colab (GPU used for AlphaFold2)

---

## 📁 Repository Structure

gene_family_identification/

├── data/
│   └── ncbi_dataset/
│
├── docs/
│   ├── literature/
│   └── reports/
│
├── domain_validation/
│
├── phylogenetic_analysis/
│
├── gene_structure/
│
├── protein_structure/
│   ├── alphafold_predictions/
│   └── validation/
│
├── gene_mapping/
│
├── duplication/
│
├── collinearity_mcscanx/
│
├── promoter_analysis/
│
├── rna_seq_project/
│   ├── data/
│   ├── results/
│   ├── scripts/
│   ├── metadata.txt
│   ├── sample_list.txt
│   └── md5sum.txt
│
├── docking/
│
├── scripts/
│
├── interpro/
│
├── Project final file.docx
├── Software Versions.txt
├── README.md
└── .gitignore


---

## 📌 Reproducibility

- Modular scripts provided
- Intermediate outputs available
- Fully reproducible workflow

---

## 👩‍🔬 Author

*Siriga Priyanka*

---

## 📌 Final Summary

This project establishes a multi-omics framework integrating:

- Genome-wide gene identification  
- Functional validation  
- Evolutionary analysis  
- Structural biology  
- Transcriptomics  

📊 Outcome:  
Identification of *stress-responsive gene networks in buckwheat*, supported by genomic and transcriptomic analyses.
