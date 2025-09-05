import h5py

filename = "/scratch/mfafouti/Transfection_assessment_Tianze/CR_count/out/Tianze_BDNF_IRES_Cellranger_marlen/outs/filtered_feature_bc_matrix.h5"

with h5py.File(filename, "r") as f:
    print("Top-level groups:", list(f.keys()))

    # Features (genes)
    print("\nFeatures available:")
    print(list(f["matrix/features"].keys()))

    # Preview first 10 gene_ids and gene_names
    gene_ids = f["matrix/features/id"][:10]
    gene_names = f["matrix/features/name"][:10]
    feature_types = f["matrix/features/feature_type"][:10]

    print("\nFirst 10 gene_ids:", [g.decode("utf-8") for g in gene_ids])
    print("First 10 gene_names:", [g.decode("utf-8") for g in gene_names])
    print("First 10 feature_types:", [g.decode("utf-8") for g in feature_types])

    # Barcodes
    barcodes = f["matrix/barcodes"][:10]
    print("\nFirst 10 barcodes:", [b.decode("utf-8") for b in barcodes])
