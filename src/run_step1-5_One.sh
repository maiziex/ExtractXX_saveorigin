set -x
filename=$1
output=$2
out_dir=$3
h5_dir=$4
ref=$5
barcode_whitelist=$6


# step 1:
python BasicXX_step1_One.py -i $filename -o $output --out_dir $out_dir

# step 2:
python BasicXX_step2_One.py -o $output --out_dir $out_dir

# step 3:

# step 4:
python BasicXX_step4.py -o $output --out_dir $out_dir -r $ref

# step 5:
python BasicXX_step5.py -o $output --out_dir $out_dir -b $barcode_whitelist --h5_dir $h5_dir



