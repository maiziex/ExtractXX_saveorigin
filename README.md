# BasicXX_One


## Dependencies:
BasicXX_One utilizes <a href="https://www.python.org/downloads/">Python3</a>, <a href="http://bio-bwa.sourceforge.net/">BWA</a>, <a href="http://samtools.sourceforge.net/">SAMtools</a>, and <a href="http://broadinstitute.github.io/picard/">Picard</a>. To be able to execute the above programs by typing their name on the command line, the program executables must be in one of the directories listed in the PATH environment variable.

## Running The Code:
### (Type "python BasicXX_One.py -h" for help information)
```
python BasicXX_One.py -i ../S_24385_Lysis_2_USPD16081850_H3332CCXY_L1 -o Lysis_24385_L1 --out_dir ../ -r refdata-GRCh38-2.1.0/fasta/genome.fa --h5_dir ../qual_20/ -b barcode4M.fa
```
```
usage: BasicXX_One.py [-h] [--input_file_prefix INPUT_FILE_PREFIX]
                      [--output_file_prefix OUTPUT_FILE_PREFIX]
                      [--out_dir OUT_DIR] [--reference REFERENCE]
                      [--h5_dir H5_DIR]
                      [--barcode_whitelist BARCODE_WHITELIST]

Run 10x Basic

optional arguments:
  -h, --help            show this help message and exit
  --input_file_prefix INPUT_FILE_PREFIX, -i INPUT_FILE_PREFIX
                        Input file prefix
  --output_file_prefix OUTPUT_FILE_PREFIX, -o OUTPUT_FILE_PREFIX
                        Output file prefix
  --out_dir OUT_DIR, -o_dir OUT_DIR
                        Directory to store outputs
  --reference REFERENCE, -r REFERENCE
                        Referece fasta files
  --h5_dir H5_DIR, -h5 H5_DIR
                        Directory to store h5 related files
  --barcode_whitelist BARCODE_WHITELIST, -b BARCODE_WHITELIST
                        Barcode white list

```

