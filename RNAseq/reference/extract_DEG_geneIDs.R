sig <- read.csv("Significant_DEGs.csv", row.names=1)

deg_ids <- rownames(sig)

write.table(
  deg_ids,
  file = "DEG_geneIDs.txt",
  quote = FALSE,
  row.names = FALSE,
  col.names = FALSE
)

cat("DEG gene IDs extracted:", length(deg_ids), "\n")