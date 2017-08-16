set -x 
input_file=$1
out_dir=$2
barcode_whitelist=$3
h5_dir=$4
Cr=$5
raw_fastq_RA=$6
raw_fastq_I1=$7
flag="all"
used_flag=$8

for i in {21..22} ;
do
    echo $i
    chr_num=chr$i
    cp run_step1.sbatch run_step1_$i.sbatch
    echo samtools view $input_file $chr_num \> $out_dir$chr_num"_rmdup.sam" >> run_step1_$i.sbatch

    echo awk -F"'\t'" "'{print "'$1'"}'" $out_dir$chr_num"_rmdup.sam" "|sort|uniq -d|grep -F -f -" $out_dir$chr_num"_rmdup.sam" \> $out_dir$chr_num"_rmdup_paired.sam" >> run_step1_$i.sbatch

    echo python create_barcode_fastq_for_sam.py $out_dir$chr_num"_rmdup_paired.sam" $out_dir$chr_num"_rmdup_paired_barcode.fastq" >> run_step1_$i.sbatch

    echo bwa mem -t 32 -k 5 -T 1 $barcode_whitelist -p $out_dir$chr_num"_rmdup_paired_barcode.fastq" \> $out_dir$chr_num"_rmdup_paired_barcode.sam" >> run_step1_$i.sbatch

    echo python write_sam_by_barcodematch_dict_and_correctbarcode.py $barcode_whitelist $out_dir$chr_num"_rmdup_paired_barcode.sam" $out_dir$chr_num"_rmdup_paired.sam" $out_dir$chr_num"_rmdup_paired_correctbarcode.sam" >> run_step1_$i.sbatch
    
    if [ $used_flag = $flag ]
    then
        echo python Extract_final_qname_byall.py $h5_dir$chr_num"_cb.h5" $out_dir$chr_num"_rmdup_paired_correctbarcode.sam" $out_dir$chr_num"_final_qname.txt" $out_dir$chr_num"_qname_barcode_dict.p" $Cr >> run_step1_$i.sbatch
    else
        echo python Extract_final_qname.py $h5_dir$chr_num"_cb.h5" $out_dir$chr_num"_rmdup_paired_correctbarcode.sam" $out_dir$chr_num"_final_qname.txt" $out_dir$chr_num"_qname_barcode_dict.p" $Cr >> run_step1_$i.sbatch
    fi

    echo python Extract_final_fastq_reads_RA.py $out_dir$chr_num"_qname_barcode_dict.p" $raw_fastq_RA $out_dir$chr_num"_RA.fastq" >>run_step1_$i.sbatch

    echo python Extract_final_fastq_reads_I1.py $out_dir$chr_num"_qname_barcode_dict.p" $raw_fastq_I1 $out_dir$chr_num"_I1.fastq" >>run_step1_$i.sbatch

 
    sbatch run_step1_$i.sbatch
 
done


