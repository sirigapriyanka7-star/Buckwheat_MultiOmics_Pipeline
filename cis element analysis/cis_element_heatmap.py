# cis_element_heatmap.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load your two-column CSV
# Replace 'cis_elements.csv' with your file name
df = pd.read_csv("cis_elements.csv")  # Columns: Gene, CRE

# Step 2: Create a pivot table counting occurrences of each CRE per gene
df_counts = df.pivot_table(index='Gene', columns='CRE', aggfunc='size', fill_value=0)

# Optional: sort CRE columns alphabetically
df_counts = df_counts.reindex(sorted(df_counts.columns), axis=1)

# Step 3: Save the counts table for reference
df_counts.to_csv("cis_counts.csv")

# Step 4: Generate heatmap
plt.figure(figsize=(14,8))
sns.heatmap(df_counts, cmap="viridis", annot=True, fmt="d", cbar_kws={'label': 'Count'})
plt.title("Cis-Regulatory Element Distribution Across Genes", fontsize=16)
plt.ylabel("Genes", fontsize=12)
plt.xlabel("Cis-Regulatory Elements (CREs)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()