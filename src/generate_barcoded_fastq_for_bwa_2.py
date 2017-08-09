#import pdb
#pdb.set_trace()
import sys

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



#generate_barcoded_fastq("lib3_H_L8.ap.RA.fastq","lib3_H_L8.ap.barcoded.fastq")
#generate_barcoded_fastq("test.fastq","test.barcoded.fastq")
if __name__ == "__main__":
    RA_file = sys.argv[1]
    output_file= sys.argv[2]
    generate_barcoded_fastq(RA_file,output_file)

