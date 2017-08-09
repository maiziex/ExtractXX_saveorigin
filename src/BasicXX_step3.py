import sys
import os

from argparse import ArgumentParser

parser = ArgumentParser(description="Run 10x Basic -- step 3: Concatenate All Fastqs Files (10X fastqs files, Barcoded fastqs files) ")
parser.add_argument('--output_file_prefix','-o', help="Output file prefix")
parser.add_argument('--out_dir','-o_dir', help="Directory to store outputs", default='../temp/')

args = parser.parse_args()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        os.system("python BasicXX_step3.py -h")
    else:
        output = open('count_files.txt','r').read()
        num_files = int(output) - 1
        
        command_5 = "./cat_fastqs.sh "  + args.out_dir + args.output_file_prefix + " " + str(num_files-1)
        os.system(command_5)

        






