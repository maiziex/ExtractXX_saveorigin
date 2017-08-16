#import pdb
#pdb.set_trace()
import pickle
import sys

def extract_fastq_reads(pickle_file,fastq_file,output_file):
    qname_barcode_dict = pickle.load(open(pickle_file, "rb"))
    f = open(fastq_file,"r")
    fw = open(output_file,"w")
    count = 0
    flag = 1
    for line in f:
        print(count)
        if flag == 0 and count%8 < 7:
            count += 1
            continue
        elif flag == 0 and count%8 == 7:
            flag = 1
            count += 1
            continue

        data = line.rsplit()
        if count%8 == 0:
            qname = data[0][1:]
            if qname in qname_barcode_dict:
                barcode = qname_barcode_dict[qname]
                fw.writelines(line)
            else:
                flag = 0
                count += 1
                continue
        elif count%8 == 1:
            read1 = data[0]
            read1_new = barcode + read1[16:]
            fw.writelines(read1_new + "\n")
        elif count%8 == 2:
            fw.writelines("+\n")
        elif count%8 == 3:
            fw.writelines(line)
        elif count%8 == 4:
            fw.writelines(line)
        elif count%8 == 5:
            fw.writelines(line)
        elif count%8 == 6:
            fw.writelines(line)
        elif count%8 == 7:
            fw.writelines(line)

        count += 1
    f.close()
    fw.close()

#extract_fastq_reads("qname_barcode_dict_lib1_2.p","/oak/stanford/groups/arend/Xin/SimProj/Final_fastqs/lib1_L/read-RA_si-CCTGGAGA_lib-001_hap-001.fastq","lib1_final_RA_2.fastq")
if __name__ == "__main__":
    qname_barcode_pickle = sys.argv[1]
    origin_fastq_RA = sys.argv[2]
    output_fastq_RA = sys.argv[3]
    extract_fastq_reads(qname_barcode_pickle,origin_fastq_RA,output_fastq_RA)

