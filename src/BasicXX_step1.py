import sys
import os

from argparse import ArgumentParser

parser = ArgumentParser(description="Run 10x Basic -- step1: Split raw fastqs files to multiple files, and generate 10X fastqs files")
parser.add_argument('--lines','-l',type=int,help="line number", default=100000000)
parser.add_argument('--input_file_prefix','-i',help="Input file prefix")
parser.add_argument('--output_file_prefix','-o', help="Output file prefix")
parser.add_argument('--out_dir','-o_dir', help="Directory to store outputs", default='../temp/')

args = parser.parse_args()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        os.system("python BasicXX_step1.py -h")
    else:
        gunzip_command_1 = "gunzip " + args.input_file_prefix + "_1.fq.gz" 
        gunzip_command_2 = "gunzip " + args.input_file_prefix + "_2.fq.gz" 
        print(gunzip_command_1)
        print(gunzip_command_2)
        os.system(gunzip_command_1 + " & " + gunzip_command_2 + " & wait")
        command_1= "split -l "  + str(args.lines) + " " + args.input_file_prefix + "_1.fq" +  "  " + args.input_file_prefix + "_1.fq" 
        command_2= "split -l "  + str(args.lines) + " " + args.input_file_prefix + "_2.fq" +  "  " + args.input_file_prefix + "_2.fq" 
        print(command_1)
        print(command_2)
        os.system(command_1 + " & " + command_2 + " & wait")
        command_3 = "ls " + args.input_file_prefix + "_1.fq* | wc -l > count_files.txt"
        os.system(command_3)
        output = open('count_files.txt','r').read()
        num_files = int(output) - 1
        
        command_4 = "./run_list.sh " + args.input_file_prefix + " " + args.out_dir + args.output_file_prefix + " " + str(num_files-1)
        print(command_4)
        os.system(command_4 + " &  wait ")


        

        






