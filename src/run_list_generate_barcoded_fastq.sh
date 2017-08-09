set -x
output_file_prefix=$1
num=$2
declare -a arr=("aa" "ab" "ac" "ad" "ae" "af" "ag" "ah" "ai" "aj" "ak" "al" "am" "an" "ao" "ap" "aq" "ar" "as" "at" "au" "av" "aw" "ax" "ay" "az" "ba" "bb" "bc" "bd" "be" "bf" "bg" "bh" "bi" "bj" "bk" "bl" "bm" "bn" "bo" "bp" "bq" "br" "bs" "bt" "bu" "bv" "bw" "bx" "by" "bz")
start=0

for j in `eval echo {$start..$num}`
do
    echo ${arr[$j]}
    i=${arr[$j]}
    cp run_generate_barcoded_fastq.sbatch run_generate_barcoded_fastq_$i.sbatch
    echo python generate_barcoded_fastq_for_bwa_2.py $output_file_prefix$i".RA.fastq" $output_file_prefix$i".barcoded.fastq" >>run_generate_barcoded_fastq_$i.sbatch
    sbatch run_generate_barcoded_fastq_$i.sbatch
 
done


