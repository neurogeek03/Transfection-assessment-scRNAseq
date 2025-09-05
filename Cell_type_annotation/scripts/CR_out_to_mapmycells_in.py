import anndata
import scipy.sparse
import pandas as pd
import scanpy as sc

# Path to the filtered matrix folder
path = "/scratch/s/shreejoy/mfafouti/TianzeData/Tianze_GFP_IRES_Cellranger_marlen/outs/filtered_feature_bc_matrix"

# Read the 10x matrix
adata = sc.read_10x_mtx(path, var_names='gene_symbols', cache=True)

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

# If 'gene_ids' is the column you want to keep:
adata.var['gene_id'] = adata.var['gene_ids']
adata.var = adata.var[['gene_id']]  # MapMyCells expects only this

# Save with gzip compression
adata.write_h5ad('tianze_IRES_mapmycells_in.h5ad', compression='gzip')

print("adata file saved!")