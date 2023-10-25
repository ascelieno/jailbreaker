#!/bin/bash
#SBATCH -A hpc2n2023-115    # Replace with your actual account ID
#SBATCH -p amd_gpu          # Use the 'amd_gpu' partition for A100 GPUs
#SBATCH --gres=gpu:a100:1   # Request 1 A100 GPU
#SBATCH --time=02:00:00     # Set a time limit

# Clear the environment from any previously loaded modules
module purge > /dev/null 2>&1

# Load necessary modules
module load GCCcore/11.3.0 Python/3.10.4 CUDA/11.7.0

# Activate the Python virtual environment
source /proj/nobackup/hpc2n2023-115/env/bin/activate

sleep 60
echo "Loading Llama 2..."

source $1
