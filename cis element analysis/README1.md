# 🧬 Promoter Sequence Retrieval and Cis-Regulatory Element Analysis

## 📌 Objective
To retrieve, clean, and analyze promoter sequences (~2000 bp upstream regions) of duplicated Fagopyrum esculentum genes and identify cis-regulatory elements (CREs) using the PLACE database.

---

## 🧬 Promoter Sequence Retrieval

Promoter sequences (~2000 bp upstream of the translation start site) were extracted for duplicated FES genes from the genome assembly.

### Initial Processing Challenges
- Genome FASTA contained duplicate scaffold IDs interfering with extraction
- Gene IDs were inconsistent across duplication pairs
- Strand-specific promoter extraction required correction

---

## ⚙️ Script Development and Modifications

A custom Python script was developed and modified to ensure accurate promoter retrieval.

### Key Improvements:
1. *Scaffold Parsing Fix*
   - Correct extraction of scaffold information from gene identifiers

2. *Coordinate-Based Extraction*
   - Used duplication-based coordinates (start, end, strand)
   - Avoided reliance on full gene IDs for accuracy

3. *Strand-Aware Promoter Extraction*
   - Positive strand: extracted 2000 bp upstream
   - Negative strand: extracted reverse-complement downstream sequence

---

## 📥 Promoter Sequence Output

- Successfully extracted *30 promoter sequences*
- Some duplication redundancy occurred due to genes appearing in multiple duplication pairs

### Example Gene Set:
- Fes_sc0011510.1.g000001.aua.1  
- Fes_sc0000499.1.g000001.aua.1  
- Fes_sc0000542.1.g000013.aua.1  
- Fes_sc0000231.1.g000023.aua.1  
- Fes_sc0008411.1.g000001.aua.1  
- Fes_sc0008411.1.g000003.aua.1  
- Fes_sc0007348.1.g000004.aua.1  
- Fes_sc0005868.1.g000004.aua.1  

(Additional duplicated entries were present due to overlapping gene pairs; total = 31 sequences)

---

## 🧹 Sequence Cleaning and Filtering

### 1. Handling Ambiguous Bases
- Long stretches of N retained (PLACE tolerates unknown bases)
- True promoter regions preserved downstream of gaps

### 2. Base Standardization
- Converted lowercase/ambiguous nucleotides to uppercase
  - Example: TTTnCAAATT → TTTNCAAATT

### 3. Duplicate Removal
- Redundant promoter sequences removed
- Final dataset:
  - *9 unique promoter sequences*

### Output File:

promoters_clean.fasta

---

## 🧪 Cis-Regulatory Element (CRE) Identification

Promoter sequences were analyzed using the *PLACE database*.

### Annotation Included:
- Motif name
- Consensus sequence
- Position in promoter
- Strand orientation
- Functional category

---

## 🧬 Types of Cis-Regulatory Elements Identified

### 1. Core Promoter Elements
- TATA box
- CAAT box
- Initiator motifs
- Polyadenylation signals

---

### 2. Transcription Factor Binding Sites
- MYB
- MYC
- DOF

---

### 3. Hormone-Responsive Elements
- Cytokinin (ARR1AT)
- ABA (ABRELATERD1, RAV1AAT)
- Auxin (ARFAT)
- Gibberellin (GAREAT)

---

### 4. Stress and Light Responsive Elements
- W-box / WRKY motifs
- GATA box
- I-box
- GT1 consensus

---

### 5. Tissue-Specific Motifs
- Root-specific
- Seed-specific
- Pollen-specific

---

### 6. Circadian Regulation Elements
- CIACADIANLELHC motifs
- Located mainly in distal promoter regions

---

## 🔥 Promoter Hotspot Mapping

Promoters showed *modular regulatory architecture* with overlapping motif clusters.

| Region (bp) | Regulatory Features |
|-------------|--------------------|
| 1–500 | Core promoter, root/seed motifs |
| 400–900 | Hormone + stress + light motifs |
| 1100–1300 | Mixed regulatory clusters |
| 1500–1800 | Seed/pollen + hormone + stress motifs |
| 1800–2000 | Core + circadian + stress motifs |

---

## 🧠 Biological Interpretation

- Promoters exhibit *combinatorial regulation*
- Multiple motifs co-localize forming regulatory hotspots
- Suggests integration of:
  - Hormonal signaling
  - Stress responses
  - Light regulation
  - Developmental control
  - Circadian rhythm

---

## 📌 Key Findings

- 30 promoter sequences extracted initially
- 9 high-quality unique promoters retained after cleaning
- Dense cis-regulatory architecture identified
- Strong evidence of multi-layered gene regulation in duplicated FES genes

---

## 📁 Output Files

- promoters_raw.fasta (initial extraction)
- promoters_clean.fasta (final dataset)
- CRE annotation tables (PLACE output)

---

## 🧠 Conclusion

This workflow successfully retrieved and curated promoter sequences from duplicated Fagopyrum esculentum genes and revealed complex cis-regulatory architectures. The presence of dense, overlapping regulatory motifs suggests that these genes are under multi-layered transcriptional control involving hormonal, environmental, and developmental signals.