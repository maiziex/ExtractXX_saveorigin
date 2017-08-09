set -x
filename=$1
file1=$1"_1.fq"
file2=$1"_2.fq"
output=$2
num=$3
declare -a arr=("aa" "ab" "ac" "ad" "ae" "af" "ag" "ah" "ai" "aj" "ak" "al" "am" "an" "ao" "ap" "aq" "ar" "as" "at" "au" "av" "aw" "ax" "ay" "az" "ba" "bb" "bc" "bd" "be" "bf" "bg" "bh" "bi" "bj" "bk" "bl" "bm" "bn" "bo" "bp" "bq" "br" "bs" "bt" "bu" "bv" "bw" "bx" "by" "bz")
start=0
for j in `eval echo {$start..$num}`
do
    echo ${arr[$j]}
    i=${arr[$j]}
    cp run_Raw_fastqs_to_longranger_fastqs.sbatch run_Raw_fastqs_to_longranger_fastqs_$i.sbatch
    echo python3 Raw_fastqs_to_longranger_fastqs_2.py $file1$i $file2$i $output$i".RA.fastq" $output$i".I1.fastq">>run_Raw_fastqs_to_longranger_fastqs_$i.sbatch
    sbatch run_Raw_fastqs_to_longranger_fastqs_$i.sbatch
 
done


