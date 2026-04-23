# 🧬 Ab Initio Protein Structure Prediction (AlphaFold2 / ColabFold)

## 🎯 Objective
To predict the 3D structures of selected buckwheat proteins using *AlphaFold2 (via ColabFold)* without relying on template-based modeling, and to evaluate structural confidence using pLDDT scores.

---

## ⚙️ Methodology

### 1. Sequence Preparation
- Protein sequences were extracted in *FASTA format*
- All sequences were checked for completeness before submission
- Only full-length, validated sequences were used for prediction

---

### 2. ColabFold Setup
- Platform: Google Colab
- Model: AlphaFold2 (ColabFold implementation)
- Runtime: GPU (T4)
- Each protein was processed in a *separate Colab session*

---

### 3. Structure Prediction Workflow
- Sequences submitted to AlphaFold2 Colab notebook
- Multiple Sequence Alignment (MSA) generated using:
  - MMseqs2_uniref_env
  - Paired + unpaired mode enabled
- 3D protein structures generated along with:
  - pLDDT confidence scores
  - Ranking of predicted models

---

### 4. Model Selection & Quality Assessment
- Top-ranked model (Rank 1) selected for each protein
- Quality evaluation based on:
  - pLDDT score (per-residue confidence)
  - Sequence coverage plots
  - Visual inspection of 3D structures

---

### 5. Runtime Notes
- Temporary Google Colab disconnections occurred during execution
- Sessions were resumed to recover intermediate outputs
- GPU availability limitations caused delays (~6-hour reset intervals)

---

### 6. Data Recording
- Screenshots captured at all key stages:
  - Sequence submission
  - Prediction progress
  - pLDDT confidence plots
  - 3D structure visualization
- Full *AlphaFold2/ColabFold output ZIP files* saved for each protein
- All outputs stored for reproducibility and downstream analysis

---

## 📊 Protein-Specific Summary

| Protein ID | Length (aa) | Mean pLDDT / Confidence | Structure Reliability | Remarks |
|------------|-------------|--------------------------|------------------------|----------|
| Fes_sc0001617.1.g000017.aua.1 | 213 | ~85–87 (High) | Reliable | Well-folded; high-confidence regions |
| Fes_sc0003471.1.g000005.aua.1 | 213 | ~80–85 (High) | Reliable | Good sequence coverage |
| Fes_sc0005868.1.g000004.aua.1 | 496 | ~83–90 (High/Moderate) | Valid | Full coverage; complete structure captured |
| Fes_sc0011510.1.g000001.aua.1 | 469 | ~85 (High) | Reliable | Structure recovered after runtime reconnect |
| Fes_sc0000231.1.g000023.aua.1 | 455 | ~80–85 (High) | Reliable | Complete structure and plots obtained |

---

## 📁 Files in This Folder
- Protein structure output ZIP files (Protein 1–5)
- Project progress documentation
- Screenshots of ColabFold execution and results

---

## 🧠 Conclusion
AlphaFold2/ColabFold predicted high-confidence 3D structures for all selected buckwheat proteins. Most proteins showed strong pLDDT scores, indicating reliable structural predictions. These results provide a structural foundation for further functional and evolutionary analysis.

---