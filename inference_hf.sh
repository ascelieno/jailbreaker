#!/bin/bash

#these two are needed for llm_qlora
ml GCCcore/11.3.0 Python/3.10.4

source $PROJ/llm_qlora/new_env/bin/activate


echo $1
echo $2
echo $3
echo $4
echo $5
echo $6
echo $7
echo $8


echo ../jailbreaker/inference_hf.py configs/$1.yaml ../jailbreaker/$2 ../jailbreaker/$3 $4 $5 $6 $7 $8


cd ../llm_qlora
#python ../jailbreaker/inference_hf2.py $1 $2 $3 $4 $5 configs/$6.yaml ../jailbreaker/$7 ../jailbreaker/$8
#python ../jailbreaker/inference_hf2.py --config_path configs/$1.yaml 
#python ../jailbreaker/inference_hf.py $1 $2 $3 $4 $5 configs/$6.yaml ../jailbreaker/$7 ../jailbreaker/$8
python ../jailbreaker/inference_hf.py configs/$1.yaml ../jailbreaker/$2 ../jailbreaker/$3 $4 $5 $6 $7 $8
