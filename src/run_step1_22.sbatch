#!/bin/bash 
#
#all commands that start with SBATCH contain commands that are just used by SLURM for scheduling
#################
#set a job name  
#SBATCH --job-name=step1
#################  
#a file for job output, you can check job progress
#SBATCH --output=step1.out
#################
# a file for errors from the job
#SBATCH --error=step1.err
#################
#time you think you need; default is 2 hours
#format could be dd-hh:mm:ss, hh:mm:ss, mm:ss, or mm
#SBATCH --time=48:00:00
#################
#quality of service; think of it as job priority
#SBATCH --partition=normal
# We are submitting to the dev partition, there are several on sherlock: normal, gpu, owners, hns, bigmem (jobs requiring >64Gigs RAM) 
# 
#################
#number of nodes you are requesting
#SBATCH --nodes=1
#################
#memory per node; default is 4000 MB per CPU
#SBATCH --mem=60000
#################

# Have SLURM send you an email when the job ends or fails, careful, the email could end up in your clutter folder
# Also, if you submit hundreds of jobs at once you will get hundreds of emails.
 
#SBATCH --mail-type=END,FAIL # notifications for job done & fail
#SBATCH --mail-user=xzhou15@stanford.edu

#now run normal batch commands
# note the "CMD BATCH is an R specific command
#module load python/3.3.2
samtools view ../../S_24385_L1_barcoded_sorted_rmdup_bybarcode.bam chr22 > ../../extract_10x/chr22_rmdup.sam
awk -F'\t' '{print $1}' ../../extract_10x/chr22_rmdup.sam |sort|uniq -d|grep -F -f - ../../extract_10x/chr22_rmdup.sam > ../../extract_10x/chr22_rmdup_paired.sam
python create_barcode_fastq_for_sam.py ../../extract_10x/chr22_rmdup_paired.sam ../../extract_10x/chr22_rmdup_paired_barcode.fastq
bwa mem -t 32 -k 5 -T 1 /scratch/users/xzhou15/SimProj_10X/RealData/Scripts/barcode4M.fa -p ../../extract_10x/chr22_rmdup_paired_barcode.fastq > ../../extract_10x/chr22_rmdup_paired_barcode.sam
python write_sam_by_barcodematch_dict_and_correctbarcode.py /scratch/users/xzhou15/SimProj_10X/RealData/Scripts/barcode4M.fa ../../extract_10x/chr22_rmdup_paired_barcode.sam ../../extract_10x/chr22_rmdup_paired.sam ../../extract_10x/chr22_rmdup_paired_correctbarcode.sam
python Extract_final_qname_byall.py ../../qual_20/chr22_cb.h5 ../../extract_10x/chr22_rmdup_paired_correctbarcode.sam ../../extract_10x/chr22_final_qname.txt ../../extract_10x/chr22_qname_barcode_dict.p 0.2
python Extract_final_fastq_reads_RA.py ../../extract_10x/chr22_qname_barcode_dict.p ../../S_24385_L1.RA.fastq ../../extract_10x/chr22_RA.fastq
python Extract_final_fastq_reads_I1.py ../../extract_10x/chr22_qname_barcode_dict.p ../../S_24385_L1.I1.fastq ../../extract_10x/chr22_I1.fastq
