#import pdb
#pdb.set_trace()
import sys

def create_barcode_fastq(sam_file,barcode_fastq):
    f = open(sam_file,"r")
    fw = open(barcode_fastq,"w")
    count = 1
    for line in f:
        data = line.rsplit()
        qname = data[0]
        barcode = data[-1].split(":")[-1].split("-")[0]
        fw.writelines("@" + qname + "\n")
        fw.writelines(barcode + "\n")
        fw.writelines("+\n")
        fw.writelines("A-<-7-<---<<F7<F\n")
        count += 1

    f.close()
    fw.close()



#create_barcode_fastq("chr22.sam","chr22_barcode.fastq")
if __name__ == "__main__":
    chr_sam_file = sys.argv[1]
    chr_barcode_fastq_file = sys.argv[2]
    create_barcode_fastq(chr_sam_file,chr_barcode_fastq_file)
