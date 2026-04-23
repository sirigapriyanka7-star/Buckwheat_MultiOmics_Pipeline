input_file = "all_vs_all_NR_with_coords.tsv"
output_file = "all_vs_all_NR_with_coords_clean.tsv"

with open(input_file) as infile, open(output_file, "w") as out:
    for line in infile:
        line = line.strip()

        # Remove quotes
        line = line.replace('"', '')

        # Fix spaces inside gene IDs → convert "Fes sc000..." → "Fes_sc000..."
        line = line.replace("Fes sc", "Fes_sc")
        line = line.replace("Fes 5c", "Fes_sc")
        line = line.replace("Tes sc", "Fes_sc")
        line = line.replace("fes sc", "Fes_sc")

        out.write(line + "\n")

print("Cleaning complete → all_vs_all_NR_with_coords_clean.tsv")