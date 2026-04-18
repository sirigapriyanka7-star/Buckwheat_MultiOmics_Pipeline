# Buckwheat Multi-Omics Pipeline

## Overview

This repository presents a comprehensive multi-omics workflow to investigate abiotic stress-responsive gene families in Fagopyrum esculentum, supported by transcriptomic evidence from Fagopyrum tataricum under drought stress conditions.

The study focuses on the CBL–CIPK–SOS calcium signaling pathway, integrating genome-wide gene identification, evolutionary analysis, transcriptomics, regulatory element analysis, protein structure prediction, and molecular docking.

---

## Objectives

- Genome-wide identification of CBL, CIPK, and SOS gene families  
- Evolutionary and gene duplication analysis  
- Promoter cis-regulatory element analysis  
- Transcriptomic profiling under drought stress  
- Protein structure prediction and validation  
- Molecular docking with phytochemicals  

---

## Biological System

- Target species: Fagopyrum esculentum (buckwheat)  
- Transcriptomic reference: Fagopyrum tataricum  
- Stress condition: Drought stress  

---

## Workflow Overview

Genome → Gene Identification → Duplication Analysis → Promoter Analysis → RNA-seq → Protein Structure → Docking → Integration  

### Stepwise Workflow

1. Genome and annotation retrieval  
2. Identification of CBL, CIPK, SOS gene families  
3. Domain and motif validation  
4. Gene duplication classification and synteny analysis  
5. Promoter cis-element analysis  
6. RNA-seq differential expression analysis  
7. Protein structure prediction using AlphaFold  
8. Molecular docking with phytochemicals  
9. Biological interpretation and integration  

---

## Key Results

### Gene Duplication
| Type | Count |
|------|------|
| Tandem | 0 |
| Proximal | 0 |
| Segmental | 31 |
| Dispersed | 0 |

---

### RNA-seq Differential Expression
- Upregulated genes: 3307  
- Downregulated genes: 3042  

---

### Molecular Docking
| Protein | Binding Energy (kcal/mol) | Interpretation |
|----------|--------------------------|----------------|
| P1 | -7.983 | Strong binding |
| P3 | -6.184 | Moderate binding |
| P5 | -6.126 | Moderate binding |
| P2 | -4.493 | Weak binding |
| P4 | +11.140 | Unfavorable |

---

## Tools Used

- BLAST+  
- InterProScan  
- MUSCLE  
- MEME Suite  
- MCScanX  
- DESeq2 (R)  
- AlphaFold / ColabFold  
- AutoDock Vina  
- PyMOL  
- Python (Matplotlib, Seaborn)  

---

## Key Findings

- CBL–CIPK–SOS pathway is highly conserved in buckwheat  
- Segmental duplication drives gene family expansion  
- Strong transcriptional reprogramming under drought stress  
- Potential phytochemical–protein interactions identified  

---

## Limitations

- Fully computational study  
- RNA-seq derived from related species (F. tataricum)  
- Docking results require experimental validation  

---

## Future Work

- Experimental validation (qPCR / wet lab)  
- CRISPR functional studies  
- Metabolomic integration  
- Field-level stress analysis  

---

## Author

Priyanka Siriga  

---

## References

Bailey, T.L. et al. (2009). MEME Suite. Nucleic Acids Research, 37, W202–W208.  
Conesa, A. et al. (2016). RNA-seq best practices. Genome Biology, 17, 13.  
Edgar, R.C. (2004). MUSCLE alignment. Nucleic Acids Research, 32, 1792–1797.  
Jumper, J. et al. (2021). AlphaFold. Nature, 596, 583–589.  
Jones, P. et al. (2014). InterProScan 5. Bioinformatics, 30, 1236–1240.  
Liao, Y. et al. (2014). featureCounts. Bioinformatics, 30, 923–930.  
Love, M.I. et al. (2014). DESeq2. Genome Biology, 15, 550.  
O’Boyle, N.M. et al. (2011). Open Babel. Journal of Cheminformatics, 3, 33.  
Trott, O. & Olson, A.J. (2010). AutoDock Vina. Journal of Computational Chemistry, 31, 455–461.  
Wang, Y. et al. (2012). MCScanX. Nucleic Acids Research, 40, e49.  
Yamaguchi-Shinozaki, K. & Shinozaki, K. (2005). Stress cis-elements. Plant Physiology, 139, 411–418.  
Zhu, J.K. (2002, 2016). Abiotic stress signaling. Annual Review of Plant Biology / Plant Journal.  

---

## Note

This pipeline is fully reproducible and designed for plant multi-omics and abiotic stress research.

