#!/bin/bash

TCGA_CASES_DIRECTORY_PATH=${1?Error: no TCGA cases directory path given}
OUTPUT_DIRECTORY_PATH=${2?Error: no output directory path given}

python label_cases.py $TCGA_CASES_DIRECTORY_PATH $OUTPUT_DIRECTORY_PATH
