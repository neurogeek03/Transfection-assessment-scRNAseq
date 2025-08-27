#!/bin/bash 
#SBATCH --account=rrg-shreejoy
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=23:00:00
#SBATCH --job-name=experimental_group_count
#SBATCH --output=/scratch/mfafouti/Transfection_assessment_Tianze/CR_count/logs/CR_count_%x_%j.txt
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mariaeleni.fafouti@mail.utoronto.ca

cd $SLURM_SUBMIT_DIR

/project/rrg-shreejoy/TianzeData/cellranger-9.0.1/bin/cellranger count \
    --id=Tianze_BDNF_IRES_Cellranger_marlen \
    --transcriptome=/scratch/mfafouti/Transfection_assessment_Tianze/CR_count/new_IRES_Mouse_Reference \
    --fastqs=/project/rrg-shreejoy/TianzeData/Tianze_raw_data/20250314_LH00244_0269_B22W7KJLT3_Tomoda_Tianze/fastq/merged \
    --sample=BDNF \
    --create-bam=true