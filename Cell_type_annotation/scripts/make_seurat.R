library(Seurat)
library(dplyr)
library(data.table)  # for fast metadata reading
library(ggplot2)

seurat_obj <- Read10X(data.dir = "/scratch/s/shreejoy/mfafouti/TianzeData/Tianze_GFP_IRES_Cellranger_marlen/outs/filtered_feature_bc_matrix") %>%
  CreateSeuratObject(project = "MyProject", min.cells = 3, min.features = 200)

metadata <- read.csv("/scratch/s/shreejoy/mfafouti/TianzeData/Tianze_GFP_IRES_Cellranger_marlen/mapmycells_out/tianze_IRES_mapmycells_in_10xWholeMouseBrain(CCN20230722)_HierarchicalMapping_UTC_1752759822181.csv", skip=4)

print(seurat_obj)

metadata <- as.data.table(metadata)
# Clean it just to use class and subclass
metadata_clean <- metadata[, .(cell_id, class_name, subclass_name)]

# Set cell_id as rownames (to match Seurat object)
metadata_clean <- as.data.frame(metadata_clean)
rownames(metadata_clean) <- metadata_clean$cell_id

# Set cell_id as rownames (to match Seurat object)
metadata_clean <- as.data.frame(metadata_clean)
rownames(metadata_clean) <- metadata_clean$cell_id

# Make sure only cells present in Seurat object are kept
metadata_subset <- metadata_clean[colnames(seurat_obj), ]

# Add to Seurat object's metadata
seurat_obj <- AddMetaData(seurat_obj, metadata = metadata_subset)

head(seurat_obj[[]][, c("class_name", "subclass_name")])

saveRDS(seurat_obj, file = "tianze_IRES_celltypes.rds")
