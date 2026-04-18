process FILTER_BLAST {

    input:
    path blast_file
    path nr_file

    output:
    path "all_vs_all_NR.tsv"

    script:
    """
    python3 /mnt/c/GeneDuplicationAnalysis/filter_blast_nr.py
    """
}