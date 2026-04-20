#!/bin/bash

echo -e "Protein\tBest_Energy(kcal/mol)" > final_results.tsv

for i in 1 2 3 4 5; do

    file="p${i}/vina_dock.pdbqt"

    if [ ! -f "$file" ]; then
        echo "Warning: $file not found"
        continue
    fi

    # Extract best binding energy (lowest value)
    best=$(grep "REMARK VINA RESULT" "$file" | awk '{print $4}' | sort -n | head -1)

    echo -e "P${i}\t${best}" >> final_results.tsv

done

echo "Results saved in final_results.tsv"

# Ranking (best to worst)
echo ""
echo "Ranking:"
sort -k2 -n final_results.tsv | column -t
