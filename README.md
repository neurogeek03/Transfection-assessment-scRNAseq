# Transfection-assessment-scRNAseq
Assessing how well a transfection worked using droplet-based scRNAseq. 

## Experiment overview: 
1 control and 1 experimental mouse sample were sequenced using 10x Genomics scRNA-seq technology. The results are aligned to the mouse reference genome. By examining the number of cells expressing various transgene, we aim to verify how well the transfection experiment has worked. 

## Alignment to the reference genome 
- The mouse reference genome can be found at: https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001635.27/ 
- However, this does not include the transgenes we have added
- Before running the alignment, we need to create a custom reference, using `CellRanger`

### "Make reference" - CellRanger 
- To do this, we need:
    1. A `.fasta` file ⇒ contains the sequence of the transgene(s) ⇒ will be aligned to the ref genome
    2. A `.gtf` file ⇒ contains the annotation of the transgene(s) ⇒ shows which regions in the FASTA correspond to exons of each gene
- Add any additional gene sequences to the main `.fasta` file + their annotations to the `.gtf`
- Here’s what matters in the gtf file:
    - The first column name should be the same in different parts like so:
      `IRES    transgene   exon    1   617     .   +   .   gene_id "IRES"; transcript_id "IRES"; gene_name "IRES"; gene_biotype "protein_coding";`
      Right above is an example of how one line (corresponds to 1 gene) should look like. 
