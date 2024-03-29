#!/bin/bash
#SBATCH -A hpc2n2023-124    # Replace with your actual account ID
#SBATCH -p amd_gpu          # Use the 'amd_gpu' partition for A100 GPUs
#SBATCH --gres=gpu:a100:1   # Request 1 A100 GPU
#SBATCH --time=100:00:00     # Set a time limit

source /proj/nobackup/hpc2n2023-124/llm_qlora/venv/bin/activate

srun python inference_hf_default.py data/questions_all.txt /proj/nobackup/hpc2n2023-124/llama/llama-2-7b-chat/hf data/results/llama2_chat_hf_default_46_questions.txt
    
