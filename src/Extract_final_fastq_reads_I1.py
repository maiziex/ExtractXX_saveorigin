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
        if flag == 0 and count%4 < 3:
            count += 1
            continue
        elif flag == 0 and count%4 == 3:
            flag = 1
            count += 1
            continue

        data = line.rsplit()
        if count%4 == 0:
            qname = data[0][1:]
            if qname in qname_barcode_dict:
                fw.writelines(line)
            else:
                flag = 0
                count += 1
                continue
        elif count%4 == 1:
            fw.writelines(line)
        elif count%4 == 2:
            fw.writelines(line)
        elif count%4 == 3:
            fw.writelines(line)

        count += 1
    f.close()
    fw.close()

#extract_fastq_reads("qname_barcode_dict_lib1_2.p","/oak/stanford/groups/arend/Xin/SimProj/Final_fastqs/lib1_L/read-I1_si-CCTGGAGA_lib-001_hap-001.fastq","lib1_final_I1_2.fastq")
if __name__ == "__main__":
    qname_barcode_pickle = sys.argv[1]
    origin_fastq_I1 = sys.argv[2]
    output_fastq_I1 = sys.argv[3]
    extract_fastq_reads(qname_barcode_pickle,origin_fastq_I1,output_fastq_I1)

