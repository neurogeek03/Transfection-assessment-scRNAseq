# Transfection-assessment-scRNAseq
Assessing how well a transfection worked using droplet-based scRNAseq. 

## Bioinformatics tools required: 
The user needs to have CellRanger, which can be easily installed following this tutorial: https://www.10xgenomics.com/support/software/cell-ranger/latest/tutorials/cr-tutorial-in


## Experiment overview: 
1 control and 1 experimental mouse sample were sequenced using 10x Genomics scRNA-seq technology. The results are aligned to the mouse reference genome. By examining the number of cells expressing various transgene, we aim to verify how well the transfection experiment has worked. 
- The mouse reference genome can be found at: https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001635.27/ 
- However, this does not include the transgenes we have added
- Before running the alignment, we need to create a custom reference, including all the genes we wish to see reads for

### 1. "Make reference" - CellRanger 
This will enable us to create a custom mouse reference genome, including all the genes we're interested in
- To do this, we need:
    1. A `.fasta` file ⇒ contains the sequence of the transgene(s) ⇒ will be aligned to the ref genome
    2. A `.gtf` file ⇒ contains the annotation of the transgene(s) ⇒ shows which regions in the FASTA correspond to exons of each gene
- Add any additional gene sequences to the main `.fasta` file + their annotations to the `.gtf`
- Here’s what matters in the gtf file:
    - The first column name should be the same in different parts like so:
      `IRES    transgene   exon    1   617     .   +   .   gene_id "IRES"; transcript_id "IRES"; gene_name "IRES"; gene_biotype "protein_coding";`
      Right above is an example of how one line (corresponds to 1 gene) should look like. 
- The command used to run this is the following:
  &nbsp;
  `cellranger_bin, "count",
        f"--id={sample_id}",
        f"--fastqs={sample_fastq}",  # Still pointing to the FASTQ location in the home directory.
        f"--transcriptome={ref_path}", # upstream path to the ref folder 
        "--create-bam=false"`

### 2. "Count" - CellRanger
This will perform alignment to the reference genome and count the number reads per gene.
    
