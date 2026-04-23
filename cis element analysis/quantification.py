import pandas as pd

# Load file (IMPORTANT: your columns are Gene + CRE)
df = pd.read_csv("cis_elements.csv")

# Rename safely
df.columns = ["Gene", "Motif"]

# Clean spaces (VERY IMPORTANT in your case)
df["Gene"] = df["Gene"].astype(str).str.replace(" ", "")
df["Motif"] = df["Motif"].astype(str).str.strip()

# Remove missing values
df = df.dropna()

# -------------------------
# QUANTIFICATION (CORRECT)
# -------------------------
cis_counts = df.groupby(["Gene", "Motif"]).size().unstack(fill_value=0)

# Save clean matrix
cis_counts.to_csv("cis_counts_clean.csv")

print("✅ Clean quantification done")
print(cis_counts)
