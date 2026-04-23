# 🧬 Buckwheat Protein–Phytochemical Docking Study

## 📌 Objective
To investigate the interaction between selected stress-responsive proteins from Fagopyrum esculentum and phytochemicals from medicinal plants using molecular docking and structural analysis.

---

## 🧪 Overview of Workflow

This study integrates protein structure prediction, ligand preparation, docking simulations, and structural visualization to identify potential bioactive interactions.

---

## 🧬 1. Protein Selection and Structure Prediction

- Five buckwheat proteins involved in stress response were selected.
- 3D structures were predicted and validated (including Ramachandran plot analysis).
- Structures were prepared in *PDB format* and converted to *PDBQT format* for docking.

### Status:
✔ Protein modeling completed  
✔ Structure validation completed  
✔ Docking-ready files generated  

---

## 🌿 2. Phytochemical Library Preparation

Three phytochemicals were selected based on antioxidant and stress-response relevance:

- Withaferin A (Withania somnifera)
- Alpha-Curcumene (Curcuma longa)
- Aloesin (Aloe vera)

### Processing Steps:
- Structures obtained in MOL2 format
- Converted to PDB and PDBQT using Open Babel
- Ligands cleaned and corrected for docking compatibility

---

## ⚙️ 3. Docking Preparation

- Protein–ligand complexes prepared for docking using AutoDock Vina and SwissDock.
- Grid parameters calculated using blind docking strategy:

### Grid Calculation:
- Center = midpoint of min/max X, Y, Z coordinates  
- Size = (max − min) + 5 Å margin  

---

## ⚠️ 4. Docking Issues and Resolution

### Initial Issues:
- PDBQT parsing errors in SwissDock
- Invalid ligand formatting (ROOT tag errors)

### Fixes Applied:
- Removed water molecules (HOH)
- Added polar hydrogens using Open Babel
- Rebuilt ligands with correct 3D geometry and charges
- Corrected file paths and batch processing loop errors

### Outcome:
✔ All protein structures successfully cleaned  
✔ All ligand files regenerated  
✔ Docking inputs validated  

---

## 🧪 5. Docking Execution (SwissDock + Vina)

### Protein–Ligand Pairing:

- P1 → Withaferin A  
- P2 → Alpha-Curcumene  
- P3 → Aloesin  
- P4 → Withaferin A  
- P5 → Alpha-Curcumene  

### Results:
- Multiple docking poses generated
- Binding energies estimated (ΔG)
- Cluster-based docking outputs obtained

---

## 🧾 6. Docking Results Summary

| Protein | Binding Energy (kcal/mol) | Status |
|--------|---------------------------|--------|
| P1 | -7.983 | Strong binding |
| P3 | -6.184 | Moderate binding |
| P5 | -6.126 | Moderate binding |
| P2 | -4.493 | Weak binding |
| P4 | +11.140 | Discarded |

---

## 🏆 7. Final Ranking

1. *P1* – Best binding affinity (lead candidate)  
2. *P3* – Secondary candidate  
3. *P5* – Secondary candidate  
4. *P2* – Weak interaction  
5. *P4* – Non-favorable interaction (excluded)

---

## 🎨 8. Docking Visualization

Completed for all 5 systems (P1–P5):

- Protein cartoon representation
- Ligand stick representation
- Binding pocket zoom views
- Surface interaction visualization
- High-resolution PNG images (300 DPI)

---

## 📁 9. Folder Organization

Each system (P1–P5) contains:

- Docking outputs (vina_dock.pdb, vina_dock.pdbqt)
- Ligand files (.mol2, .pdbqt)
- Protein structures (hydrogen-added PDB files)
- Configuration files
- Visualization images

---

## 🧠 Conclusion

This study successfully identifies *P1 as the most promising protein target*, with strong binding affinity to phytochemicals. P3 and P5 serve as secondary candidates for further investigation.

All docking, visualization, and structural preparation steps are completed.