library(pheatmap)

vsd <- vst(dds)
mat <- assay(vsd)

top <- head(order(rowVars(mat), decreasing=TRUE), 50)

pheatmap(mat[top, ], scale="row")