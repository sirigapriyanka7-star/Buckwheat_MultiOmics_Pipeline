# 🧬 Gene Mapping and Chromosomal Distribution (MG2C Analysis)

## 📌 Objective
To map CBL and CIPK genes onto their respective scaffolds/chromosomes of Fagopyrum esculentum and visualize their chromosomal distribution using MG2C (Map Gene2Chromosome).

---

## 📁 Input Data

- Gene annotation table:
  - Gene table for MG2C.txt
  - Includes gene IDs, scaffold/chromosome IDs, start positions, end positions, and color codes

- Scaffold/chromosome length file:
  - Chromosome scaffold length for mg2c.txt
  - Contains total lengths of scaffolds/chromosomes used for scaling

- Project documentation:
  - Project progress (7) 1 (2).docx

---

## ⚙️ Methodology

### 1. Gene Table Preparation
- A structured gene table was created containing:
  - Gene ID  
  - Scaffold / chromosome ID  
  - Start position (bp)  
  - End position (bp)  
  - Visualization color coding  

---

### 2. Chromosome Length File Preparation
- Scaffold/chromosome lengths were compiled separately
- This ensured proper scaling of gene positions during visualization

---

### 3. Gene Mapping Using MG2C
- MG2C (Map Gene2Chromosome) tool was used for visualization
- Gene positions were mapped along scaffolds/chromosomes in kilobases (Kb)
- Each gene was labeled with its corresponding gene ID

---

## 📊 Results

- All CBL and CIPK genes were successfully mapped onto scaffolds/chromosomes
- The final visualization accurately represents:
  - Gene distribution across scaffolds
  - Relative gene positions
  - Chromosomal organization patterns

---

## 🖼️ Visualization Output

- MG2C generated chromosomal distribution diagrams
- SVG export option was available but did not function properly in this case
- Therefore, *screenshots were taken for documentation and analysis*

### 📌 Visualization Settings
- Font styles customized for clarity  
- Color coding applied for gene differentiation  
- Container sizes and scaling adjusted for readability  
- Proper scaling ensured accurate gene positioning  

---

## 🧠 Interpretation

- Genes are unevenly distributed across scaffolds
- Some scaffolds contain higher gene density, indicating possible gene clustering
- Mapping provides a clear overview of genomic organization of CBL and CIPK families
- Results support downstream evolutionary and functional analysis

---

## 📁 Files in This Folder

- Gene table for MG2C.txt — gene coordinate dataset  
- Chromosome scaffold length for mg2c.txt — scaffold size information  
- Project progress (7) 1 (2).docx — analysis documentation  
- MG2C visualization screenshots (gene distribution maps)  

---

## 🧰 Tools Used

- MG2C (Map Gene2Chromosome)
- Manual gene table curation
- Scaffold length preprocessing

---

## 📌 Conclusion

MG2C-based mapping successfully visualized the chromosomal distribution of CBL and CIPK genes in Fagopyrum esculentum. Despite SVG export limitations, screenshot-based outputs provide a clear and reliable representation of gene localization across scaffolds.