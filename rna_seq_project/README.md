RNA-seq Differential Expression Analysis Pipeline

This folder contains a complete and reproducible RNA-seq analysis workflow for identifying differentially expressed genes (DEGs) between drought and control conditions.

---

📌 Overview

This workflow includes end-to-end RNA-seq analysis starting from raw sequencing data to differential expression results and visualization. Drought stress was analyzed against control conditions to identify transcriptomic changes using a standardized computational pipeline.

This workflow is fully reproducible using the provided scripts and input data.

---

🧬 Dataset

Drought condition

- SRR29434873
- SRR29434877

Control condition

- SRR29434880
- SRR29434881

---

⚙️ Workflow Summary

1. Data acquisition (NCBI/SRA datasets)
2. Quality control using FastQC
3. Read alignment using HISAT2
4. Gene quantification using featureCounts
5. Metadata preparation (condition grouping)
6. Differential expression analysis using DESeq2
7. Visualization (volcano plot and heatmap)

---

🧪 Tools and Software Used

- HISAT2 (read alignment)
- SAMtools (BAM sorting)
- featureCounts (gene quantification)
- FastQC (quality control)
- R (DESeq2, ggplot2, pheatmap)

R packages:

- DESeq2
- ggplot2
- pheatmap

---

📊 Key Findings

- Drought stress induced widespread transcriptional reprogramming
- Clear separation observed between drought and control samples
- Thousands of genes showed significant differential expression
- Balanced distribution of upregulated and downregulated genes identified

Example Top Differentially Expressed Genes

- g87.t1
- g97.t1
- g137.t1
- g17.t1
- g10.t1

These genes showed strong differential expression and may play important roles in drought stress response mechanisms.

---

📁 Project Structure / Files Present

📂 Input Data

- data/ → Raw sequencing files
- ncbi_dataset/ → Downloaded NCBI dataset files
- Fagopyrum.gtf → Reference genome annotation file
- genome.fa → Reference genome sequence file
- md5sum.txt → File integrity check

🧬 Alignment & Quantification

- SRR29434873_sorted.bam → Drought sample alignment
- SRR29434877_sorted.bam → Drought sample alignment
- SRR29434880_sorted.bam → Control sample alignment
- SRR29434881_sorted.bam → Control sample alignment
- gene_counts.txt → Gene-level count matrix (featureCounts output)
- gene_counts.txt.summary → featureCounts summary report

📊 Metadata & Support Files

- metadata.txt → Sample condition information
- sample_list.txt → List of samples used in analysis
- RData → Saved R workspace/session

📈 Output Results

- results/ → Differential expression analysis outputs
- DEG_results.csv → Full DESeq2 results
- significant_DEGs.csv → Significant genes (padj < 0.05)
- upregulated_genes.csv → Upregulated genes in drought condition
- downregulated_genes.csv → Downregulated genes in drought condition
- functional_summary.csv → Gene-level summary classification
- volcano_plot.pdf → Differential expression visualization
- heatmap.png → Expression heatmap of top variable genes

---

🧪 Scripts Used

prefetch.sh

fastqc.sh

hisat2.sh

featurecounts.sh

deseq2_analysis.R

heatmap.R


All scripts are modular and can be executed independently to reproduce each step of the RNA-seq analysis pipeline.
---

📌 Summary

This folder contains a complete RNA-seq analysis pipeline from raw sequencing data to processed results, statistical analysis, and visualization. The workflow provides a reproducible framework for studying drought-induced transcriptomic changes and identifying candidate genes for further biological investigation.