# Gene Structure Analysis of CBL and CIPK Genes in Fagopyrum esculentum

## 🧬 Objective
To analyze the exon–intron organization and structural features of CBL (Calcineurin B-like) and CIPK (CBL-interacting protein kinase) genes in buckwheat using genome annotation data and GSDS visualization.

---

## 📊 Input Data
- Buckwheat genome annotation file (GFF3 format)
- Non-redundant list of CBL and CIPK genes identified from prior analyses

---

## ⚙️ Methodology

### Gene Structure Extraction
- Gene annotation records were retrieved from the GFF3 file
- Extracted features:
  - Gene start and end positions
  - Exon coordinates
  - Coding sequence (CDS) regions
  - Scaffold information
- Number of exons determined from exon entries
- CDS ranges recorded to confirm coding regions

### Motif Mapping
- Previously identified conserved motifs were mapped onto gene structures
- Exon-wise distribution of motifs was analyzed

---

## 🔬 Results

### Gene Structure Features
- CBL genes contain *8–9 exons*, indicating relatively complex structure  
- CIPK genes show high variation:
  - Some genes contain *1–3 exons*
  - Others contain *up to 14 exons*
- Structural diversity suggests functional divergence within the CIPK family

---

## 📋 Gene Structure Summary (Table 6)

| Gene ID | Family | Scaffold | CDS Range (bp) | Exons |
|--------|--------|----------|----------------|-------|
| Fes_sc0001617.1.g000017.aua.1 | CBL | sc0001617.1 | 109063–112331 | 9 |
| Fes_sc0003471.1.g000005.aua.1 | CBL | sc0003471.1 | 31301–35241 | 8 |
| Fes_sc0005868.1.g000004.aua.1 | CBL | sc0005868.1 | 23449–27158 | 9 |
| Fes_sc0011510.1.g000001.aua.1 | CIPK | sc0011510.1 | 541–1950 | 2 |
| Fes_sc0000542.1.g000013.aua.1 | CIPK | sc0000542.1 | 56556–57854 | 2 |
| Fes_sc0000231.1.g000023.aua.1 | CIPK | sc0000231.1 | 108183–109781 | 3 |
| Fes_sc0008411.1.g000001.aua.1 | CIPK | sc0008411.1 | 3048–4403 | 1 |
| Fes_sc0008411.1.g000003.aua.1 | CIPK | sc0008411.1 | 16741–18057 | 1 |
| Fes_sc0007348.1.g000004.aua.1 | CIPK | sc0007348.1 | 11573–15470 | 14 |
| Fes_sc0010474.1.g000002.auf.1 | CIPK | sc0010474.1 | 3917–7977 | 12 |
| Fes_sc0000499.1.g000001.aua.1 | CIPK | sc0000499.1 | 5199–9012 | 14 |

---

## 🧩 Gene Structure Visualization (GSDS 2.0)

### Input Preparation
- Custom GFF3 files manually constructed for each gene
- Included:
  - Gene
  - Transcript (mRNA)
  - Exon features
- Parent-child relationships defined using Parent attribute
- Files formatted according to GFF3 specifications

### Visualization Settings
- Introns: black lines (1 px), no rescaling  
- Exons: grey rounded rectangles (10 px height)  
- UTRs: blue rectangles (8 px height)  

### Output
- Gene structure diagrams generated using GSDS 2.0
- Introns inferred automatically from exon positions
- Figures exported in PDF format

---

## 🧠 Interpretation
- CBL genes exhibit conserved exon–intron organization  
- CIPK genes show structural diversity, indicating evolutionary expansion  
- Motif mapping aligns with exon structure, supporting functional conservation  
- Gene structure variation may reflect regulatory complexity differences  

---

## 📁 Files in This Folder
- project_progress.docx → Gene structure analysis workflow documentation  
- gsds_structure.pdf → GSDS visualization of CBL and CIPK genes  
- gsds.cbl_structure.pdf → GSDS visualization of CBL genes  

---

## 🧰 Tools Used
- GFF3 genome annotation (Kazusa Buckwheat Genome Database)  
- GSDS 2.0 (Gene Structure Display Server)  

---

## 📌 Conclusion
Gene structure analysis reveals conserved exon organization in CBL genes and structural diversity in CIPK genes. This supports functional conservation and evolutionary diversification of the CBL–CIPK signaling system in Fagopyrum esculentum.