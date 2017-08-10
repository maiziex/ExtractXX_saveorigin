# step 4: # align, rmdup, filter by qual20
filename=$1 
out_dir=$2
reference=$3  


mkdir ../temp_bwa
bwa mem -t 32 -C $reference -p $out_dir$filename".barcoded.fastq"  | samtools view -bS - | samtools sort -T ../temp_bwa/temp_sorting -o $out_dir$filename"_barcoded_sorted.bam" 
samtools index $out_dir$filename"_barcoded_sorted.bam"  
rm -rf ../temp_bwa

mkdir ../temp
java -jar /scratch/users/xzhou15/Software/picard.jar MarkDuplicates INPUT=$out_dir$filename"_barcoded_sorted.bam" OUTPUT=$out_dir$filename"_barcoded_sorted_rmdup_bybarcode.bam" METRICS_FILE=../sorted.bam_rmdup.txt REMOVE_DUPLICATES=true VALIDATION_STRINGENCY=LENIENT TMP_DIR=../temp READ_ONE_BARCODE_TAG=BX READ_TWO_BARCODE_TAG=BX
samtools index $out_dir$filename"_barcoded_sorted_rmdup_bybarcode.bam"
rm -rf ../temp

samtools view -bq 20 $out_dir$filename"_barcoded_sorted_rmdup_bybarcode.bam" > $out_dir$filename"_barcoded_sorted_rmdup_bybarcode_filter_by_qual20.bam" 
samtools index $out_dir$filename"_barcoded_sorted_rmdup_bybarcode_filter_by_qual20.bam" 

