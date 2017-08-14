set -x 
input_file=$1
qual20_dir=$2
barcode_whitelist=$3
for i in {1..22} X;
do
    echo $i
    chr_num=chr$i
    cp run_step5.sbatch run_step5_$i.sbatch
    echo samtools view $input_file $chr_num \> $qual20_dir$chr_num".sam" >> run_step5_$i.sbatch
 
    echo python create_barcode_fastq_for_sam.py $qual20_dir$chr_num".sam" $qual20_dir$chr_num"_barcode.fastq" >>run_step5_$i.sbatch

    echo bwa mem -t 32 -k 5 -T 1 $barcode_whitelist -p $qual20_dir$chr_num"_barcode.fastq" \> $qual20_dir$chr_num"_barcode.sam" >> run_step5_$i.sbatch

    echo python write_sam_by_barcodematch_dict_and_correctbarcode.py $barcode_whitelist $qual20_dir$chr_num"_barcode.sam" $qual20_dir$chr_num".sam" $qual20_dir$chr_num"_correctbarcode.sam" >> run_step5_$i.sbatch

    echo python Cal_Cf_Cr_from_sorted_bam_final_2.py $qual20_dir$chr_num"_correctbarcode.sam" $qual20_dir$chr_num"_cb.h5" >>run_step5_$i.sbatch
 
    sbatch run_step5_$i.sbatch
 
done


