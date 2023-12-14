#!/bin/bash
#SBATCH -A hpc2n2023-124    # Replace with your actual account ID
#SBATCH -p amd_gpu          # Use the 'amd_gpu' partition for A100 GPUs
#SBATCH --gres=gpu:a100:1   # Request 1 A100 GPU
#SBATCH --time=02:00:00     # Set a time limit

srun python inference_hf_default.py    
