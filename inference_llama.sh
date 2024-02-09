#!/bin/bash

# Clear the environment from any previously loaded modules
module purge > /dev/null 2>&1

# Load necessary modules
module load GCCcore/11.3.0 Python/3.10.4 CUDA/11.7.0

# Activate the Python virtual environment
source /proj/nobackup/hpc2n2023-124/env/bin/activate

echo "Loading Llama 2..."

cd /proj/nobackup/hpc2n2023-124/llama
pwd

echo $1
echo $2
echo $3
echo $4
echo $5
echo $6
echo $7
echo $8
echo $9

torchrun --nproc_per_node 1 ../jailbreaker/inference_llama_text.py \
	--ckpt_dir $1/ \
	--input_file ../jailbreaker/$2 \
	--output_file ../jailbreaker/$3 \
	--tokenizer_path tokenizer.model \
	$4 $5 $6 $7 $8 $9 \



#chat completion
#torchrun --nproc_per_node 1 ../jailbreaker/inference_llama_chat.py \
#	--ckpt_dir llama-2-7b-chat/ \
#	--tokenizer_path tokenizer.model \
#	--max_seq_len 1024 --max_batch_size 64 --temperature=0.7 --top_p=0.95 \ 
#	--input_file ../jailbreaker/data/questions_all.json \
#	--output_file ../jailbreaker/data/results/llama2_7b_chat_original_45_questions.txt
