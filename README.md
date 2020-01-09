# tcga-mutation-labeler
Tool for labeling .SVS files from TCGA cases into true/false-directories based on a specific mutation provided by a mutation list.

## How to run

1. Download the project

1. Navigate to the `src` directory by using the terminal

    `cd my/path/to/tcga-mutation-labeler/src`

1. Give execute permission to the script

    `chmod +x ./run_labeler.sh`
    
1. Run the script

    `./run_labeler.sh FULL_PATH_TO_TCGA_DOWNLOADS_FOLDER FULL_PATH_TO_MUTATION_FILE MUTATION_OF_INTEREST OUTPUT_DIRECTORY_PATH DESIRED_DISK_OPERATION`
    
    Here is an example of a run
    
    `./run_labeler.sh /home/user/debuggingtissue/tcga_cases /home/user/debuggingtissue/TCGA-PRAD.mutect2_snv.tsv SPOP /home/user/debuggingtissue/output_of_labelling -move`

  
### Description of input parameters
 
 * `FULL_PATH_TO_TCGA_DOWNLOADS_FOLDER`
 
    * Full path to download folder of TCGA files
 
 * `FULL_PATH_TO_MUTATION_FILE`
 
    * Full path to download folder of TCGA mutation file list
 
 * `MUTATION_OF_INTEREST`
 
    * Gene that you wish to base your labeling on (e.g SPOP)
 
 * `OUTPUT_DIRECTORY_PATH`
    * Full path to the directory where you wish to store the labeled files 
 
 * `DESIRED_DISK_OPERATION`
    * How you wish to perform the disk operations. Permitted operations:
      * `-copy`
        * Copies the files from the `FULL_PATH_TO_TCGA_DOWNLOADS_FOLDER` to the `OUTPUT_DIRECTORY_PATH`. Slower than `-move` operation.
      * `-move`
        * Moves the files from the `FULL_PATH_TO_TCGA_DOWNLOADS_FOLDER` to the `OUTPUT_DIRECTORY_PATH`.
      
