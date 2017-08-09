set -x
output_file_prefix=$1
num=$2
declare -a arr=("aa" "ab" "ac" "ad" "ae" "af" "ag" "ah" "ai" "aj" "ak" "al" "am" "an" "ao" "ap" "aq" "ar" "as" "at" "au" "av" "aw" "ax" "ay" "az" "ba" "bb" "bc" "bd" "be" "bf" "bg" "bh" "bi" "bj" "bk" "bl" "bm" "bn" "bo" "bp" "bq" "br" "bs" "bt" "bu" "bv" "bw" "bx" "by" "bz")
start=0
for j in `eval echo {$start..$num}`
do
    echo ${arr[$j]}
    i=${arr[$j]}
    cat $output_file_prefix$i".barcoded.fastq">>$output_file_prefix".barcoded.fastq"
    cat $output_file_prefix$i".RA.fastq">>$output_file_prefix".RA.fastq"
    cat $output_file_prefix$i".I1.fastq">>$output_file_prefix".I1.fastq"
done
