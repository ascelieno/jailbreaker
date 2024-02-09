# Clear the environment from any previously loaded modules
module purge > /dev/null 2>&1

# Load necessary modules
module load GCCcore/11.3.0 Python/3.10.4 CUDA/11.7.0

# Activate the Python virtual environment
source /proj/nobackup/hpc2n2023-124/env/bin/activate

echo "Loading Llama 2..."

# Run the torch command with srun
srun torchrun --nproc_per_node 1 ../jailbreaker/inference_llama_text_completion.py \
--ckpt_dir llama-2-7b-chat/ \
--tokenizer_path tokenizer.model \
--max_seq_len 1024 --max_batch_size 64 \
 --input_file ../jailbreaker/data/questions_all.txt

