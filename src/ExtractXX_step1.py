import sys
import os

from argparse import ArgumentParser

parser = ArgumentParser(description="Run 10x Extract -- step1")
parser.add_argument('--input_file','-i', help="input bam file")
parser.add_argument('--out_dir','-o_dir', help="Directory to store outputs", default='./temp_extact/')
parser.add_argument('--h5_dir','-h5_dir', help="Directory for storing h5 files of molecules")
parser.add_argument('--barcode_whitelist','-b', help="Barcode white list")
parser.add_argument('--Cr','-c', help="Read coverage per molecule")
parser.add_argument('--fastq_RA','-f1', help="origin fastq reads file")
parser.add_argument('--fastq_I1','-f2', help="origin fastq index file")
parser.add_argument('--flag','-flag', help="all or subset")

args = parser.parse_args()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        os.system("python ExtractXX_step1.py -h")
    else:
        if not os.path.exists(args.out_dir):
            os.system("mkdir " + args.out_dir)
        if args.flag == "all":
            print("use flag -all")
        else:
            args.flag = "subset"

        command_1 = "./ExtractXX_step1.sh "  + args.input_file  + " " + args.out_dir + " " + args.barcode_whitelist + " " + args.h5_dir + " " + args.Cr + " " + args.fastq_RA + " " + args.fastq_I1 + " " + args.flag
        os.system(command_1)

        






