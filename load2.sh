#!/bin/bash
#SBATCH -A hpc2n2023-115    # Replace with your actual account ID
#SBATCH -p amd_gpu          # Use the 'amd_gpu' partition for A100 GPUs
#SBATCH --gres=gpu:a100:1   # Request 1 A100 GPU
#SBATCH --time=01:00:00     # Set a time limit

# Clear the environment from any previously loaded modules
module purge

# Load necessary modules
module load GCCcore/11.3.0 Python/3.10.4 CUDA/11.6.0


# Activate the Python virtual environment
source /proj/nobackup/hpc2n2023-115/env/bin/activate

# Run the torch command with srun
srun torchrun --nproc_per_node 1 /proj/nobackup/hpc2n2023-115/jailbreaker/chat.py \
    --ckpt_dir /proj/nobackup/hpc2n2023-115/llama/llama-2-7b-chat/ \
    --tokenizer_path /proj/nobackup/hpc2n2023-115/llama/tokenizer.model \
    --max_seq_len 512 --max_batch_size 6

