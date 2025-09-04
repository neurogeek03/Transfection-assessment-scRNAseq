#!/bin/bash
#SBATCH --job-name=CB_run_tianze_GFP_gpu         # Job name
#SBATCH --account=def-shreejoy  
#SBATCH --output=single_gpu_job_%j.out    # Output file (%j = job ID)
#SBATCH --nodes=1                         # Request 1 node
#SBATCH --gpus-per-node=1                 # Request 1 GPU
#SBATCH --output=/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/logs/%x_%A_%a.out
#SBATCH --error=/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/logs/%x_%A_%a.err
#SBATCH --time=03:00:00                   # Max runtime (30 minutes)

cd /scratch/mfafouti/Transfection_assessment_Tianze/CB_run
# Parameters 
CONTAINER_PATH=/scratch/mfafouti/Transfection_assessment_Tianze/CB_run/cellbender_cells.sif
# Load the Apptainer module
        module load StdEnv/2023                     # Load default environment
        module load apptainer/1.3.4                    # Adjust version if needed

apptainer exec --nv $CONTAINER_PATH python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('Device count:', torch.cuda.device_count()); print('Device name:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None')"

nvidia-smi

apptainer exec --nv $CONTAINER_PATH cellbender remove-background \
                 --cuda \
                 --input /scratch/mfafouti/Transfection_assessment_Tianze/CR_count/out/Tianze_GFP_IRES_Cellranger_marlen/raw_feature_bc_matrix.h5 \
                 --output /scratch/mfafouti/Transfection_assessment_Tianze/CB_run/OUT_gpu/GFP_CB_output.h5 \
                 --epochs 150