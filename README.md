# ExtractXX
Alternatively, for big raw fastqs files, it can also use <a href="https://github.com/maiziex/BasicXX">BasicXX</a> by five steps.

## Dependencies:
BasicXX_One utilizes <a href="https://www.python.org/downloads/">Python3</a>, <a href="http://bio-bwa.sourceforge.net/">BWA (Align Fastqs Files)</a>, <a href="http://samtools.sourceforge.net/">SAMtools</a>, and <a href="http://broadinstitute.github.io/picard/">Picard (Remove PCR duplicates)</a>. To be able to execute the above programs by typing their name on the command line, the program executables must be in one of the directories listed in the PATH environment variable.

## Running The Code:

```
python ExtractXX_step1.py -i ../../S_24385_L1_barcoded_sorted_rmdup_bybarcode.bam -f1 ../../S_24385_L1.RA.fastq -f2 ../../S_24385_L1.I1.fastq -b /scratch/users/xzhou15/SimProj_10X/RealData/Scripts/barcode4M.fa --out_dir ../../extract_10x/ --h5_dir ../../qual_20/ --Cr 0.2 --flag all 
```
```
usage: ExtractXX_step1.py [-h] [--input_file INPUT_FILE] [--out_dir OUT_DIR]
                          [--h5_dir H5_DIR]
                          [--barcode_whitelist BARCODE_WHITELIST] [--Cr CR]
                          [--fastq_RA FASTQ_RA] [--fastq_I1 FASTQ_I1]
                          [--flag FLAG]

Run 10x Extract -- step1

optional arguments:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE, -i INPUT_FILE
                        input bam file
  --out_dir OUT_DIR, -o_dir OUT_DIR
                        Directory to store outputs
  --h5_dir H5_DIR, -h5_dir H5_DIR
                        Directory for storing h5 files of molecules
  --barcode_whitelist BARCODE_WHITELIST, -b BARCODE_WHITELIST
                        Barcode white list
  --Cr CR, -c CR        Read coverage per molecule
  --fastq_RA FASTQ_RA, -f1 FASTQ_RA
                        origin fastq reads file
  --fastq_I1 FASTQ_I1, -f2 FASTQ_I1
                        origin fastq index file
  --flag FLAG, -flag FLAG
                        all or subset

```

