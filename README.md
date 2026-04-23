# 🧬 Collinearity and Synteny Analysis Using MCScanX

## 📌 Objective
To identify collinearity and syntenic relationships in Fagopyrum esculentum gene sequences using MCScanX based on protein FASTA files, gene position data, and BLASTP results.

---

## 🛠️ Software Selection

MCScanX was selected because:
- It runs offline  
- Does not require BED format  
- Accepts protein FASTA, gene position file, and BLASTP output  
- Generates:
  - Collinear blocks  
  - Synteny tables  
  - Dotplots and HTML visualizations  

---

## 💻 Computational Environment

- Windows 11  
- WSL (Ubuntu) for Linux execution  
- MCScanX compiled from source inside WSL  

This setup was used to avoid Windows binary compatibility issues.

---

## 📁 Project Folder Organization

Working directory:

C:\mcscan_project

WSL directory:

~/mcscan_project

Files were copied into WSL home directory to avoid permission issues from /mnt/c/.

---

## 📥 Input File Preparation

### 1. Protein FASTA
*FES_protein.fasta*
- Contains protein sequences of all genes  
- Gene IDs retained from original dataset  

---

### 2. Gene Position File (GFF Conversion)

Original GFF format was incompatible with MCScanX.

Converted using:

fix_gff.py

Final file:

FES_genes.gff

Required format:

Chromosome   Gene_ID   Start   End

---

### 3. BLASTP File

All-vs-all BLASTP was performed using protein FASTA.

FES_genes.blast

Validation:
- 12-column BLAST format confirmed  
- Includes identity, alignment length, E-value, and bit score  

---

## 🔧 File Format Normalization

- Windows (CRLF) → Linux (LF) conversion issues resolved  
- Files moved to WSL home directory  
- Ensured MCScanX compatibility  

---

## ⚙️ MCScanX Installation

Windows binary failed:

cannot execute binary file: Exec format error

### Solution: Compile from source

```bash
git clone https://github.com/wyp1125/MCScanX.git
cd MCScanX
make

✔ Compilation successful
✔ Core module ready for analysis


---

▶️ Running MCScanX

Command used:

./MCScanX/MCScanX FES


---

📊 Output Files

FES.collinearity

FES.html



---

📈 Results Interpretation

1. MCScanX Output

BLAST pairs imported successfully

No collinear gene blocks detected



---

2. BLAST Statistics

Total BLAST hits:

73


---

3. Gene Consistency Check

Gene IDs were consistent across:

FASTA

GFF

BLAST



---

4. Biological Interpretation

MCScanX requires:

Larger gene sets

Higher genomic density

Multiple homologous regions


In this dataset:

Small gene family was analyzed

No collinear blocks is a biologically valid result

Not a pipeline error



---

📁 Files Included

FES_protein.fasta

FES_genes.blast

FES_genes_gff.pos

FES_genes.collinearity



---

🧠 Conclusion

The MCScanX pipeline was successfully executed in a WSL environment. Although no collinearity blocks were detected, this reflects the limited size of the gene dataset rather than a technical issue. The workflow is fully reproducible and ready for scaling to larger genomic datasets.