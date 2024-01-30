#!/bin/bash

#these two are needed for llm_qlora
ml GCCcore/11.3.0 Python/3.10.4

source $PROJ/llm_qlora/venv/bin/activate

cd ../llm_qlora
python ../jailbreaker/inference_hf.py configs/llama2_7b_uncensored_original.yaml ../jailbreaker/$1 ../jailbreaker/$2 $3 $4 $5
