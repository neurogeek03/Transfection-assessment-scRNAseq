import scanpy as sc
import h5py
import numpy as np
import anndata as ad
import matplotlib.pyplot as plt
import scipy.sparse as sp
import os

out_dir = "/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/sanity_check"
os.makedirs(out_dir, exist_ok=True)

# Load raw Cell Ranger matrix
adata_raw = sc.read_10x_h5(
    "/scratch/mfafouti/Transfection_assessment_Tianze/CR_count/out/Tianze_BDNF_IRES_Cellranger_marlen/outs/raw_feature_bc_matrix.h5"
)

# Load CellBender output via h5py
cb_h5_path = "/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/OUT_2/BDNF_CB_output.h5"
with h5py.File(cb_h5_path, "r") as f:
    matrix = f['matrix']
    
    data = matrix['data'][:]
    indices = matrix['indices'][:]
    indptr = matrix['indptr'][:]
    shape = tuple(matrix['shape'][:])  # convert HDF5 dataset to tuple
    
    barcodes = [b.decode('utf-8') for b in matrix['barcodes'][:]]
    features = [f.decode('utf-8') for f in matrix['features']['name'][:]]
    
    # Reconstruct sparse matrix
    X_cb_csc = sp.csc_matrix((data, indices, indptr), shape=shape)

    # converting to CSR (cells x genes)
    X_cb = X_cb_csc.T.tocsr()

# Wrap in AnnData
adata_cb = ad.AnnData(X_cb)
adata_cb.obs_names = barcodes
adata_cb.var_names = features

print(adata_cb)

# Save the AnnData object
adata_cb.write(os.path.join(out_dir, "adata_cb.h5ad"))


