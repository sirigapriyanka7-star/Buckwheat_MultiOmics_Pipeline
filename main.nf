nextflow.enable.dsl=2

workflow {

    clean_ch = Channel.fromPath("InputFiles/all_vs_all_NR_clean.tsv")

    DUPLICATION(clean_ch)
}

include { DUPLICATION } from './modules/duplication.nf'
