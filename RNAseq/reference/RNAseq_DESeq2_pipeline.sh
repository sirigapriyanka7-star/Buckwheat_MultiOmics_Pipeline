#!/bin/bash

echo "===================================="
echo " Reproducible RNA-seq + DESeq2 Pipeline "
echo "===================================="

set -e

# =========================
# Step 1: Define inputs
# =========================

GTF="Fagopyrum_exons.gtf"
SAMPLES="samples.csv"

PAIRED_BAMS="SRR29434879_sorted.bam SRR29434877_sorted.bam"
SINGLE_BAMS="SRR29434881_2_sorted.bam SRR29434873_2_sorted.bam"

echo "Using annotation: $GTF"
echo "Using sample sheet: $SAMPLES"

# =========================
# Step 2: featureCounts (Paired-end)
# =========================

echo "Running featureCounts for paired-end samples..."

featureCounts \
-a $GTF \
-o counts_paired.txt \
-p \
$PAIRED_BAMS

echo "Paired-end counts completed"

# =========================
# Step 3: featureCounts (Single-end)
# =========================

echo "Running featureCounts for single-end samples..."

featureCounts \
-a $GTF \
-o counts_single.txt \
$SINGLE_BAMS

echo "Single-end counts completed"

# =========================
# Step 4: Summary check
# =========================

echo "Checking outputs..."

ls -lh counts_.txt

# =========================
# Step 5: DESeq2 execution (R script call)
# =========================

echo "Running DESeq2 analysis..."

Rscript DESeq2_analysis.R

echo "DESeq2 analysis completed"

# =========================
# Step 6: Final outputs
# =========================

echo "Final results generated:"
ls -lh DEG_results.csv Significant_DEGs.csv

echo "===================================="
echo " PIPELINE COMPLETED SUCCESSFULLY "
echo "===================================="