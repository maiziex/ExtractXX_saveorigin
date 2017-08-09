# step 1:
#python BasicXX_step1.py -l 100000000 -i ../S_24385_Lysis_2_USPD16081850_H3332CCXY_L1 -o S_24385_L1. --out_dir ../

# step 2:
#python BasicXX_step2.py -o S_24385_L1. --out_dir ../

# step 3:
#python BasicXX_step3.py -o S_24385_L1. --out_dir ../

# step 4:
python BasicXX_step4.py -o S_24385_L1. --out_dir ../ -r /scratch/users/xzhou15/refdata-GRCh38-2.1.0/fasta/genome.fa

# step 5:
#python BasicXX_step5.py -o Xin --out_dir ../ -b /scratch/users/xzhou15/SimProj_10X/RealData/Scripts/barcode4M.fa --h5_dir ../qual_20/



