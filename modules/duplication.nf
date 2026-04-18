process DUPLICATION {

    input:
    path clean_file

    output:
    path "duplication_types.tsv"

    script:
    """
    python3 <<EOF
from collections import Counter
import os

input_file = "$clean_file"
output_file = "duplication_types.tsv"

counts = Counter()

print("Reading file:", input_file)

with open(input_file) as f:
    for line in f:
        cols = line.strip().split("\\t")

        if len(cols) < 3:
            continue

        # Try last column as duplication type
        dup_type = cols[-1]

        counts[dup_type] += 1

print("Counts:", counts)

# WRITE OUTPUT FILE
with open(output_file, "w") as out:
    out.write("Type\\tCount\\n")
    for k, v in counts.items():
        out.write(f"{k}\\t{v}\\n")

print("File written:", os.path.abspath(output_file))
EOF

    ls -lh
    """
}
