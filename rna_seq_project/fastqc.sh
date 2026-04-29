mkdir -p qc_reports

fastqc SRR29434880_1.fastq SRR29434880_2.fastq -o qc_reports -t 4

 fastqc data/fastq/SRR29434877_1.fastq.gz data/fastq/SRR29434877_2.fastq.gz -o results/fastqc/

 fastqc data/fastq/SRR29434881_1.fastq data/fastq/SRR29434881_2.fastq -o results/fastqc/

fastqc data/fastq/SRR29434873_1.fastq.gz -o results/fastqc/
fastqc data/fastq/SRR29434873_2.fastq.gz -o results/fastqc/
