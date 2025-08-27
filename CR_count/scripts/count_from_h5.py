import h5py
import scanpy as sc 

# Path to your .h5 file
# experimental
#h5_file = "/scratch/mfafouti/Transfection_assessment_Tianze/CR_count/out/Tianze_BDNF_IRES_Cellranger_marlen/outs/filtered_feature_bc_matrix.h5"
# control
h5_file = "/scratch/mfafouti/Transfection_assessment_Tianze/CR_count/out/Tianze_GFP_IRES_Cellranger_marlen/filtered_feature_bc_matrix.h5"

# # Open the file in read-only mode
# with h5py.File(h5_file, "r") as f:
#     print("Top-level groups in file:")
#     print(list(f.keys()))

#     # Explore one group (e.g. the first one)
#     first_key = list(f.keys())[0]
#     print(f"\nPreview of '{first_key}':")
#     print(list(f[first_key].keys()))

#     # If there are datasets, preview shapes and types
#     for key in f[first_key].keys():
#         obj = f[first_key][key]
#         if isinstance(obj, h5py.Dataset):
#             print(f"Dataset {key}: shape={obj.shape}, dtype={obj.dtype}")
#             print("Preview:", obj[0:5])  # show first 5 rows

adata = sc.read_10x_h5(h5_file)

print(adata)
print(adata.var.head())   # gene info
print(adata.obs.head())   # cell/barcode info
genes_of_interest = ["IRES", "ppBdnf", "Venus"]

for gene in genes_of_interest:
    if gene in adata.var_names:
        expr = adata[:, gene].X
        n_expressing = (expr > 0).sum()
        print(f"{gene}: {n_expressing} cells expressing")
    else:
        print(f"{gene} not found in dataset")
