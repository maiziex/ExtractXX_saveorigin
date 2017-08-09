# BasicXX


## Dependencies:
BasicXX utilizes 

## Running The Code:
### Step 1: (Type "python BasicXX_step1.py -h" for help information)
```
python BasicXX_step1.py -l 100000000 -i ../S_24385_Lysis_2_USPD16081850_H3332CCXY_L1 -o S_24385_L1. --out_dir ../
```
```
usage: BasicXX_step1.py [-h] [--lines LINES]
                        [--input_file_prefix INPUT_FILE_PREFIX]
                        [--output_file_prefix OUTPUT_FILE_PREFIX]
                        [--out_dir OUT_DIR]

Run 10x Basic -- step1: Split raw fastqs files to multiple files, and generate
10X fastqs files

optional arguments:
  -h, --help            show this help message and exit
  --lines LINES, -l LINES
                        line number
  --input_file_prefix INPUT_FILE_PREFIX, -i INPUT_FILE_PREFIX
                        Input file prefix
  --output_file_prefix OUTPUT_FILE_PREFIX, -o OUTPUT_FILE_PREFIX
                        Output file prefix
  --out_dir OUT_DIR, -o_dir OUT_DIR
                        Directory to store outputs
```

### Step 2: (Type "python BasicXX_step2.py -h" for help information)
```
python BasicXX_step2.py -o S_24385_L1. --out_dir ../
```
```
usage: BasicXX_step2.py [-h] [--output_file_prefix OUTPUT_FILE_PREFIX]
                        [--out_dir OUT_DIR]

Run 10x Basic -- step 2: Generate Barcoded Fastqs Files --------------------
will call run_list_generate_barcoded_fastq.sh and
generate_barcoded_fastq_for_bwa_2.py

optional arguments:
  -h, --help            show this help message and exit
  --output_file_prefix OUTPUT_FILE_PREFIX, -o OUTPUT_FILE_PREFIX
                        Output file prefix
  --out_dir OUT_DIR, -o_dir OUT_DIR
                        Directory to store outputs
```

### Step 3: (Type "python BasicXX_step3.py -h" for help information)
```
python BasicXX_step3.py -o S_24385_L1. --out_dir ../
```

```
usage: BasicXX_step3.py [-h] [--output_file_prefix OUTPUT_FILE_PREFIX]
                        [--out_dir OUT_DIR]

Run 10x Basic -- step 3: Concatenate All Fastqs Files (10X fastqs files,
Barcoded fastqs files)

optional arguments:
  -h, --help            show this help message and exit
  --output_file_prefix OUTPUT_FILE_PREFIX, -o OUTPUT_FILE_PREFIX
                        Output file prefix
  --out_dir OUT_DIR, -o_dir OUT_DIR
                        Directory to store outputs
```

### Step 4: (Type "python BasicXX_step4.py -h" for help information)
```
python BasicXX_step4.py -o S_24385_L1. --out_dir ../ -r /scratch/users/xzhou15/refdata-GRCh38-2.1.0/fasta/genome.fa
```

```
usage: BasicXX_step4.py [-h] [--output_file_prefix OUTPUT_FILE_PREFIX]
                        [--out_dir OUT_DIR] [--reference REFERENCE]

Run 10x Basic -- step 4: BWA(align), Picard(rmdup), Samtools(filter by qual20)

optional arguments:
  -h, --help            show this help message and exit
  --output_file_prefix OUTPUT_FILE_PREFIX, -o OUTPUT_FILE_PREFIX
                        output file prefix
  --out_dir OUT_DIR, -o_dir OUT_DIR
                        Directory to store outputs
  --reference REFERENCE, -r REFERENCE
                        Referece fasta files
```

### Step 5: (Type "python BasicXX_step5.py -h" for help information)
```
python BasicXX_step5.py -o Xin --out_dir ../ -b /scratch/users/xzhou15/SimProj_10X/RealData/Scripts/barcode4M.fa --h5_dir ../qual_20/
```

```
usage: BasicXX_step5.py [-h] [--output_file_prefix OUTPUT_FILE_PREFIX]
                        [--out_dir OUT_DIR] [--h5_dir H5_DIR]
                        [--barcode_whitelist BARCODE_WHITELIST]

Run 10x Basic -- step 5: a) create fastq only for barcode, b) align barcode c)
correct barcode d) generate .h5 file

optional arguments:
  -h, --help            show this help message and exit
  --output_file_prefix OUTPUT_FILE_PREFIX, -o OUTPUT_FILE_PREFIX
                        output file prefix
  --out_dir OUT_DIR, -o_dir OUT_DIR
                        Directory to store outputs
  --h5_dir H5_DIR, -h5 H5_DIR
                        Directory to store h5 related files
  --barcode_whitelist BARCODE_WHITELIST, -b BARCODE_WHITELIST
                        Barcode white list
```
