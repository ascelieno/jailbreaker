#!/bin/bash

# Clear the environment from any previously loaded modules
module purge > /dev/null 2>&1

# Load necessary modules
module load GCCcore/11.3.0 Python/3.10.4 CUDA/11.7.0

# Activate the Python virtual environment
source /proj/nobackup/hpc2n2023-124/env/bin/activate

echo "Loading Llama 2..."

# Run the torch command with srun
#srun torchrun --nproc_per_node 1 /proj/nobackup/hpc2n2023-124/jailbreaker/example_chat_completion.py \
#    --ckpt_dir /proj/nobackup/hpc2n2023-124/llama/llama-2-7b-chat/ \
#    --tokenizer_path /proj/nobackup/hpc2n2023-124/llama/tokenizer.model \
#    --max_seq_len 1024 --max_batch_size 6 


#reads from input- and writes to output-file

#text completion
cd /proj/nobackup/hpc2n2023-124/llama
pwd

echo $1
echo $2
echo $3
echo $4
echo $5
echo $6

torchrun --nproc_per_node 1 ../jailbreaker/inference_llama_text.py \
	--ckpt_dir $1/ \
	--tokenizer_path tokenizer.model \
	--max_batch_size 64 \
	$2 $3 $4 \
	--input_file ../jailbreaker/$5 \
	--output_file ../jailbreaker/$6



#chat completion
#torchrun --nproc_per_node 1 ../jailbreaker/inference_llama_chat.py \
#	--ckpt_dir llama-2-7b-chat/ \
#	--tokenizer_path tokenizer.model \
#	--max_seq_len 1024 --max_batch_size 64 --temperature=0.7 --top_p=0.95 \ 
#	--input_file ../jailbreaker/data/questions_all.json \
#	--output_file ../jailbreaker/data/results/llama2_7b_chat_original_45_questions.txt
