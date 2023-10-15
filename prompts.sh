#!/bin/bash

#extract prompts from HTML-file and delimit with "---"
perl -0777 -ne 'print "$1\n---\n" while (/<p>(.*?)<\/p>/sg)' prompts.html > prompts.txt

#replace " with '
sed -i 's/\"/\x27/g' prompts.txt

#write to JSON format
python txt2json.sh 
