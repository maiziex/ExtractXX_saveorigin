# step 4: # align, rmdup, filter by qual20
filename=$1 
out_dir=$2
reference=$3  


mkdir ../temp_bwa
bwa mem -t 32 -C $reference -p $out_dir$filename".barcoded.fastq"  | samtools view -bS - | samtools sort -T ../temp_bwa/temp_sorting -o $out_dir$filename"_barcoded_sorted.bam" 
samtools index $out_dir$filename"_barcoded_sorted.bam"  
rm -rf ../temp_bwa

