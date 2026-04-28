# Domain Validation, Redundancy Removal, and Phylogenetic Analysis of CIPK Gene Family in Fagopyrum esculentum

## 🧬 Objective
To identify, validate, and classify CIPK (CBL-Interacting Protein Kinase) family members in buckwheat using BLASTp, domain analysis, redundancy removal, and phylogenetic analysis.

---

Arabidopsis CIPK1–CIPK26 proteins were used as queries to identify homologs in buckwheat. Multiple significant hits were obtained with high sequence identity, query coverage, and conserved domain architecture (Ser/Thr kinase + NAF/FISL domains).

---

## ⚙️ Redundancy Removal (BLASTp- and Domain-based)

### Rationale
Due to high conservation of CIPKs, multiple Arabidopsis queries matched the same buckwheat protein. To avoid overestimation of gene numbers, redundancy removal was performed.

### Criteria
- Lowest E-value  
- Highest sequence identity  
- Highest query coverage  
- Presence of canonical domains:
  - N-terminal kinase domain (PF00069)
  - C-terminal NAF/FISL domain (PF03822)

### Key Decisions

- *Fes_sc0011510.1.g000001.aua.1* → Retained as CIPK12  
- *Fes_sc0000542.1.g000013.aua.1* → Retained as CIPK20  
- *Fes_sc0000231.1.g000023.aua.1* → Retained as CIPK5  
- *Fes_sc0008411.1.g000001.aua.1* → Retained as CIPK10  
- *Fes_sc0008411.1.g000003.aua.1* → Retained as CIPK11  
- *Fes_sc0007348.1.g000004.aua.1* → Retained as CIPK23  
- *Fes_sc0010474.1.g000002.auf.1* → Retained as CIPK1  
- *Fes_sc0000499.1.g000001.aua.1* → Retained as CIPK3  

All other mappings were removed as redundant.

---

## 🔬 Distinction Between Redundancy and Gene Duplication
- Proteins with different IDs were retained as separate genes  
- Redundancy removal applied only when multiple queries mapped to the same protein  
- Paralogs on the same scaffold were retained if independently supported  

---

## 📌 Final Outcome
A non-redundant, high-confidence set of buckwheat CIPK genes was obtained, ensuring accurate gene family size estimation.

---

## 🌳 Phylogenetic Analysis

### Multiple Sequence Alignment (MSA)
- Tool: MUSCLE (EMBL-EBI)
- Input: Non-redundant buckwheat CIPKs + Arabidopsis CIPKs
- Output format: PHYLIP (interleaved)

### Phylogenetic Tree Construction
- Tree built using MUSCLE-aligned sequences  
- Arabidopsis CIPKs used as reference markers  

### Interpretation
- Buckwheat CIPKs clustered with Arabidopsis proteins  
- Clades used to assign functional subgroups  
- Example: CIPK24 (SOS2) used as a functional reference  
- Clustering indicates conserved function and orthology  

---

## 🧠 Conclusion
CIPK proteins in Fagopyrum esculentum show strong conservation in sequence, domain architecture, and evolutionary relationships with Arabidopsis CIPKs. Redundancy removal ensured accurate gene identification, and phylogenetic analysis supported functional classification.

---

## 📁 Files in This Folder
- cipk_fasta.docx – CIPK sequences used for phylogenetic analysis  
- cbl_fasta.docx – CBL sequences used for phylogenetic analysis  
- Project progress documentation
