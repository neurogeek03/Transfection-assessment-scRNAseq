import scanpy as sc

# Load the two h5 files
raw = sc.read_10x_h5("/scratch/mfafouti/Transfection_assessment_Tianze/CR_count/out/Tianze_BDNF_IRES_Cellranger_marlen/outs/filtered_feature_bc_matrix.h5")
filt = sc.read_10x_h5("/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/OUT_gpu/BDNF_CB_output_filtered.h5")

print("Raw matrix:", raw.shape)       # (n_cells, n_genes)
print("Filtered matrix:", filt.shape)

# Compare barcodes
raw_barcodes = set(raw.obs_names)
filt_barcodes = set(filt.obs_names)

print("Number of barcodes in raw:", len(raw_barcodes))
print("Number of barcodes in filtered:", len(filt_barcodes))
print("Overlap:", len(raw_barcodes & filt_barcodes))

# Find which barcodes were removed
removed = raw_barcodes - filt_barcodes
print("Removed barcodes:", len(removed))

# Optionally, write removed barcodes to file
with open("removed_barcodes.txt", "w") as f:
    for bc in removed:
        f.write(bc + "\n")

