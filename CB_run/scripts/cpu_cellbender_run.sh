#!/bin/bash
#SBATCH --job-name=CB_run_tianze_cpu         # Job name
#SBATCH --account=def-shreejoy  
#SBATCH --output=/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/logs/%x_%A_%a.out
#SBATCH --error=/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/logs/%x_%A_%a.err
#SBATCH --nodes=1                         # Request 1 node
#SBATCH --time=24:00:00                   # Max runtime

cd /scratch/mfafouti/Transfection_assessment_Tianze/CB_run

# Parameters 
CONTAINER_PATH=/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/cellbender.sif

# Load the Apptainer module
module load StdEnv/2023
module load apptainer/1.3.4

# Run CellBender on CPU (no --nv)
apptainer exec $CONTAINER_PATH cellbender remove-background \
    --input /scratch/mfafouti/Transfection_assessment_Tianze/CR_count/out/Tianze_BDNF_IRES_Cellranger_marlen/outs/raw_feature_bc_matrix.h5 \
    --output /scratch/mfafouti/Transfection_assessment_Tianze/CB_run/OUT/cpu_BDNF_CB_output.h5 \
    --epochs 150
