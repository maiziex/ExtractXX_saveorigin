import sys
import os

from argparse import ArgumentParser

parser = ArgumentParser(description="Run 10x Basic -- step 5: a) create fastq only for barcode, b) align barcode c) correct barcode d) generate .h5 file ")
parser.add_argument('--output_file_prefix','-o', help="output file prefix")
parser.add_argument('--out_dir','-o_dir', help="Directory to store outputs", default='../temp/')
parser.add_argument('--h5_dir','-h5', help="Directory to store h5 related files", default='../temp_h5/')
parser.add_argument('--barcode_whitelist','-b', help="Barcode white list")

args = parser.parse_args()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        os.system("python BasicXX_step5.py -h")
    else:
        if not os.path.exists(args.h5_dir):
            os.system("mkdir " + args.h5_dir)
        
        command_1 = "./BasicXX_step5.sh "  + args.out_dir + args.output_file_prefix + "_barcoded_sorted_rmdup_bybarcode_filter_by_qual20.bam" + " " + args.h5_dir + " " + args.barcode_whitelist
        os.system(command_1)

        






