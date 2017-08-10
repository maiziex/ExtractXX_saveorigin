import sys
import os

from argparse import ArgumentParser


parser = ArgumentParser(description="Run 10x Basic ")
parser.add_argument('--input_file_prefix','-i',help="Input file prefix")
parser.add_argument('--output_file_prefix','-o', help="Output file prefix")
parser.add_argument('--out_dir','-o_dir', help="Directory to store outputs", default='../temp_BasicXX/')
parser.add_argument('--reference','-r', help="Referece fasta files")
parser.add_argument('--h5_dir','-h5', help="Directory to store h5 related files", default='../temp_h5/')
parser.add_argument('--barcode_whitelist','-b', help="Barcode white list")

args = parser.parse_args()



if __name__ == "__main__":
    if len(sys.argv) == 1:
        os.system("python BasicXX_One.py -h")
    else:
        os.system("run_step1-5_One.sh " + args.input_file_prefix + " " + args.output_file_prefix + " " + args.out_dir + " " +args.h5_dir + " " + args.reference + " " + args.barcode_whitelist)
        


        

        






