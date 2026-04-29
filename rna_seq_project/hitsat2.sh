hisat2 -p 4 \
-x genome_index \
-1 SRR29434880_1.fastq \
-2 SRR29434880_2.fastq \
| samtools view -bS - \
| samtools sort -o SRR29434880.bam
 hisat2 -x genome_index \
-1 data/fastq/SRR29434881_1.fastq \
-2 data/fastq/SRR29434881_2.fastq \
| samtools view -bS - \
| samtools sort -o SRR29434881_sorted.bam
hisat2 -x genome_index \
-1 data/fastq/SRR29434873_1.fastq.gz \
-2 data/fastq/SRR29434873_2.fastq.gz \
| samtools view -bS - \
| samtools sort -o SRR29434873_sorted.bam
hisat2 -x genome_index \
-1 data/fastq/SRR29434877_1.fastq.gz \
-2 data/fastq/SRR29434877_2.fastq.gz \
| samtools view -bS - \
| samtools sort -o SRR29434877_sorted.bam
