# 🧬 Cis-Element Quantification and Visualization in FES/CIPK Promoters

## 📌 Objective
To quantify and visualize cis-regulatory elements (CREs) across promoter regions of duplicated Fagopyrum esculentum CBL/CIPK genes, and identify regulatory hotspots and motif conservation patterns.

---

## 📊 Gene–CRE Table Construction

- A gene–cis-element mapping table was created
- Each promoter sequence was scanned for known cis-regulatory motifs
- Every motif occurrence was assigned to its corresponding gene

### Output:
- Presence/absence matrix of motifs across genes
- Frequency-based motif count table

---

## 📈 Heatmap Visualization

A heatmap was generated to visualize cis-element distribution across promoters.

### Tools Used:
- Python
  - pandas
  - seaborn
  - matplotlib.pyplot

### What was visualized:
- Motif presence/absence across 8 promoter sequences
- Relative distribution of cis-elements across genes
- Regulatory hotspot regions

---

## 🔥 Key Observations

### Conserved Motifs (Present in most/all genes):
- ABRE (ABA-responsive element)
- MYB binding sites
- Light-responsive elements (G-box, I-box, GT1)

👉 Indicates shared regulatory control across FES/CIPK genes.

---

### Gene-Specific Motifs:
- DOF binding sites
- Gibberellin-responsive elements
- Circadian regulation motifs

👉 Suggests functional specialization among duplicated genes.

---

## 📊 Output Files

- cis_counts.csv → cis-element frequency table
- Heatmap figure (publication-ready visualization)

---

## 🧠 Biological Interpretation

- Promoter regions show both *conserved and divergent regulatory elements*
- Conserved motifs (ABRE, MYB, light-responsive) suggest shared stress and environmental regulation
- Gene-specific motifs indicate *functional divergence after duplication*
- Regulatory hotspots suggest *combinatorial transcriptional control*

---

## 📌 Conclusion

Cis-element analysis reveals that duplicated FES/CIPK genes are regulated by a combination of conserved stress-responsive motifs and gene-specific regulatory elements. This supports both *functional conservation and specialization* within the gene family.

---

## 📊 Figure Caption

*Distribution of major cis-regulatory elements across eight FES/CIPK gene promoters.*
Hotspots indicate regions of potential combinatorial regulation.