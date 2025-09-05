import scanpy as sc
import scipy
import os 

# Path to CellBender output
filename ="GFP_CB_output_filtered.h5"
name = "GFP"
path_base = "/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/OUT_gpu/"
path = os.path.join(path_base, filename)

# Output directory
out_dir = "/scratch/mfafouti/Transfection_assessment_Tianze/Cell_type_annotation/out"

# Read the CellBender h5 (10x-style HDF5)
adata = sc.read_10x_h5(path)

print(adata)

# Ensure matrix is sparse
adata.X = scipy.sparse.csr_matrix(adata.X)

# -----------------------------
# obs must have 'cell_id' column
# -----------------------------
adata.obs = adata.obs.copy()
adata.obs['cell_id'] = adata.obs.index
adata.obs = adata.obs[['cell_id']]  # MapMyCells expects only this

# -----------------------------
# var must have 'gene_id' column
# -----------------------------
adata.var = adata.var.copy()

# CellBender files usually have both 'gene_ids' and 'gene_names'.
# Keep the Ensembl IDs as 'gene_id'
if 'gene_ids' in adata.var.columns:
    adata.var['gene_id'] = adata.var['gene_ids']
elif 'gene_id' not in adata.var.columns:
    raise ValueError("No gene_ids column found in var")

adata.var = adata.var[['gene_id']]  # MapMyCells expects only this

print(adata)

# Save as h5ad
adata.write_h5ad(f"{name}_mapmycells_in.h5ad", compression="gzip")

print("adata file saved from CellBender output!")