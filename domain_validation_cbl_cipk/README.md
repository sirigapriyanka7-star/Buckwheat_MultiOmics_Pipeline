# 🧬 Domain Validation of CBL and CIPK Gene Families in Fagopyrum esculentum

## 📁 Folder: domain_validation

---

## 🧪 Overview
This folder contains domain-based functional validation of Calcineurin B-like (CBL) proteins and CBL-interacting protein kinases (CIPKs) identified in Fagopyrum esculentum through BLASTp-based homology analysis.

The objective of this module is to confirm protein identity and functional classification using conserved domain architecture analysis.

---

## 🎯 Objectives
- Validate candidate CBL proteins using conserved EF-hand calcium-binding domains
- Validate CIPK proteins using kinase and regulatory domains
- Confirm functional annotation using InterProScan
- Support BLASTp-based gene family identification with domain evidence

---

## ⚙️ Methods

### 🔹 Domain Analysis Tool
- InterProScan was used for protein domain prediction and functional annotation

### 🔹 CBL Protein Validation
- Confirmed presence of:
  - EF-hand calcium-binding motifs
  - Calcineurin B-like protein family signatures
- Verified absence of kinase domains (distinguishes from CIPKs)

### 🔹 CIPK Protein Validation
- Confirmed presence of:
  - N-terminal serine/threonine protein kinase domain
  - C-terminal NAF/FISL regulatory domain
- Verified absence of EF-hand domains (distinguishes from CBLs)

---

## 🧠 Functional Interpretation
- CBL proteins function as *calcium sensors*
- CIPK proteins function as *calcium-dependent kinases*
- Together they form the *CBL–CIPK signaling module*, involved in stress and ion homeostasis regulation

---

## 📊 Key Findings
- All CBL candidates contain conserved EF-hand domains
- All CIPK candidates contain kinase + NAF/FISL domains
- Domain architecture strongly supports BLASTp-based gene family assignments
- No misclassification between CBL and CIPK families observed

---

## 📁 Files in This Folder

- *BLAST_alignments_CBL_CIPK.docx*  
  BLASTp alignment results for CBL and CIPK gene families, including identity, coverage, and E-values.

- *BLAST_and_InterPro_CBL_CIPK.docx*  
  Combined BLASTp and InterProScan results for functional and structural validation of candidate proteins.

- *Project_Progress.docx*  
  Stepwise documentation of workflow, including filtering criteria, redundancy removal, and analysis progression.

---

## 🧪 Tools Used
- BLASTp (Kazusa BGDB)
- InterProScan
- NCBI Protein Database
- Gene Ontology (GO) annotation

---

## 📌 Notes
- This module focuses only on domain validation of pre-identified gene family members
- Full BLAST discovery pipeline is documented in the main project directory
- Results support conservation of calcium signaling pathways in buckwheat

---

## 👩‍🔬 Author
Priyanka Siriga