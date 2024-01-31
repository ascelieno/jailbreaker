#!/bin/bash

#these two are needed for llm_qlora
ml GCCcore/11.3.0 Python/3.10.4

source $PROJ/llm_qlora/venv/bin/activate

cd ../llm_qlora
python ../jailbreaker/inference_hf.py $1 $2 $3 $4 $5 configs/$6.yaml ../jailbreaker/$7 ../jailbreaker/$8
