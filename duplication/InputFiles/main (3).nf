nextflow.enable.dsl=2

/*
========================================================
 BUCKWHEAT MULTI-OMICS PIPELINE
 Journal + GitHub Ready Nextflow Workflow
========================================================
Modules:
1. BLAST (gene similarity)
2. FILTER_BLAST (NR filtering)
3. DUPLICATION (classification)
========================================================
*/

workflow {

    /*
    ----------------------------------------------------
    INPUT CHANNELS
    ----------------------------------------------------
    */

    proteins_ch = Channel.fromPath("InputFiles/proteins.fasta")
    blast_ch    = Channel.fromPath("InputFiles/all_vs_all.tsv")
    nr_ch       = Channel.fromPath("InputFiles/non_redundant_genes.txt")

    /*
    ----------------------------------------------------
    1. BLAST MODULE
    (ONLY if you already have blast module implemented)
    ----------------------------------------------------
    */

    // BLAST step optional if already done externally
    // BLAST(proteins_ch)

    /*
    ----------------------------------------------------
    2. FILTER BLAST MODULE
    ----------------------------------------------------
    */

    FILTER_BLAST(blast_ch, nr_ch)

    /*
    ----------------------------------------------------
    3. DUPLICATION MODULE
    ----------------------------------------------------
    */

    DUPLICATION()
}

/*
========================================================
 MODULE IMPORTS
========================================================
*/

include { FILTER_BLAST } from './modules/filter_blast.nf'
include { DUPLICATION }   from './modules/duplication.nf'

// Optional (only if you created it)
// include { BLAST } from './modules/blast.nf'