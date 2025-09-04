import scanpy as sc
import h5py
import numpy as np
import anndata as ad
import matplotlib.pyplot as plt
import scipy.sparse as sp
import os

out_dir = "/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/sanity_check"

adata_cb = sc.read_h5ad("/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/sanity_check/adata_cb.h5ad")
raw_path = "/scratch/mfafouti/Transfection_assessment_Tianze/CR_count/out/Tianze_BDNF_IRES_Cellranger_marlen/outs/raw_feature_bc_matrix.h5"
adata_raw = sc.read_10x_h5(raw_path)

print(adata_cb)

umis_raw = adata_raw.X.sum(axis=1).A1 if sp.issparse(adata_raw.X) else adata_raw.X.sum(axis=1)
umis_cb  = adata_cb.X.sum(axis=1).A1 if sp.issparse(adata_cb.X) else adata_cb.X.sum(axis=1)

plt.figure(figsize=(6,4))
plt.hist(umis_raw, bins=100, alpha=0.5, label='Raw')
plt.hist(umis_cb, bins=100, alpha=0.5, label='CellBender')
plt.xlabel("Total UMIs per cell")
plt.ylabel("Number of cells")
plt.yscale('log')
plt.axvline(100, color='red', linestyle='--', label='UMI cutoff')
plt.legend()
plt.title("UMIs per cell: Raw vs CellBender")
plt.savefig(os.path.join(out_dir, "comparison_umis_per_cell.png"))

genes_raw = (adata_raw.X > 0).sum(axis=1).A1 if sp.issparse(adata_raw.X) else (adata_raw.X > 0).sum(axis=1)
genes_cb  = (adata_cb.X > 0).sum(axis=1).A1 if sp.issparse(adata_cb.X) else (adata_cb.X > 0).sum(axis=1)

plt.figure(figsize=(6,4))
plt.hist(genes_raw, bins=100, alpha=0.5, label='Raw')
plt.hist(genes_cb, bins=100, alpha=0.5, label='CellBender')
plt.xlabel("Genes detected per cell")
plt.ylabel("Number of cells")
plt.yscale('log')
plt.legend()
plt.title("Genes per cell: Raw vs CellBender")
plt.savefig(os.path.join(out_dir, "comparison_genes_per_cell.png"))



# umis_per_cell = adata_cb.X.sum(axis=1).A1 if sp.issparse(adata_cb.X) else adata_cb.X.sum(axis=1)
# plt.hist(umis_per_cell, bins=100)
# plt.xlabel("Total UMIs per cell")
# plt.ylabel("Number of cells")
# plt.yscale('log')
# plt.title("Distribution of total UMIs per cell")
# plt.savefig(os.path.join(out_dir, "total_umis_per_cell.png"))

# genes_per_cell = (adata_cb.X > 0).sum(axis=1).A1 if sp.issparse(adata_cb.X) else (adata_cb.X > 0).sum(axis=1)
# plt.hist(genes_per_cell, bins=100)
# plt.xlabel("Genes detected per cell")
# plt.ylabel("Number of cells")
# plt.yscale('log')
# plt.title("Distribution of genes detected per cell")
# plt.savefig(os.path.join(out_dir, "genes_per_cell.png"))