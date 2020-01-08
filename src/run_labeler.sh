#!/bin/bash

TCGA_CASES_DIRECTORY_PATH=${1?Error: no TCGA cases directory path given}
MUTATION_FILE_PATH=${2?Error: no mutation file path given}
MUTATION_OF_INTEREST=${3?Error: no mutation of interest given}
OUTPUT_DIRECTORY_PATH=${4?Error: no output directory path given}

python label_cases.py $TCGA_CASES_DIRECTORY_PATH $MUTATION_FILE_PATH $MUTATION_OF_INTEREST $OUTPUT_DIRECTORY_PATH
