import sys
import os

from argparse import ArgumentParser

parser = ArgumentParser(description="Run 10x Basic -- step 4: BWA(align), Picard(rmdup), Samtools(filter by qual20)")
parser.add_argument('--output_file_prefix','-o', help="output file prefix")
parser.add_argument('--out_dir','-o_dir', help="Directory to store outputs", default='../temp/')
parser.add_argument('--reference','-r', help="Referece fasta files")

args = parser.parse_args()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        os.system("python BasicXX_step4.py -h")
    else:
        
        command_1 = "./BasicXX_step4.sh "  + args.output_file_prefix + " " + args.out_dir + " " + args.reference
        os.system(command_1)

        






