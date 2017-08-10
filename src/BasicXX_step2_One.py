import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter 

parser = ArgumentParser(description= '''Run 10x Basic -- step 2: Generate Barcoded Fastqs Files ''')
parser.add_argument('--output_file_prefix','-o', help="Output file prefix")
parser.add_argument('--out_dir','-o_dir', help="Directory to store outputs", default='../temp/')

args = parser.parse_args()


def generate_barcoded_fastq(fastq_10x_RA,output_file):
    f = open(fastq_10x_RA,"r")
    fw = open(output_file,"w")
    count = 0
    for line in f:
        print(count)
        if count%8 == 0:
            qname = line.rsplit()[0]
        elif count%8 == 1:
            barcode = line[:16]
            read1 = line[23:]
        elif count%8 == 3:
            read1_qual = line[23:]
        elif count%8 == 5:
            read2 = line
        elif count%8 == 7:
            read2_qual = line
            fw.writelines(qname + "\t" + "BX:Z:" + barcode + "-1" + "\n")
            fw.writelines(read1)
            fw.writelines("+\n")
            fw.writelines(read1_qual)
            fw.writelines(qname + "\t" + "BX:Z:" + barcode + "-1" + "\n")
            fw.writelines(read2)
            fw.writelines("+\n")
            fw.writelines(read2_qual)
        count += 1
    f.close()
    fw.close()




if __name__ == "__main__":
    if len(sys.argv) == 1:
        os.system("python BasicXX_step2_One.py -h")
    else:
        generate_barcoded_fastq(args.out_dir + args.output_file_prefix + ".RA.fastq",  args.out_dir + args.output_file_prefix + ".barcoded.fastq")
        

        






