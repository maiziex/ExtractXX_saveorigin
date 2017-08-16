#import pdb
#pdb.set_trace()
from collections import defaultdict
import pickle
import random
import math
import sys

def Extract_qname(h5_file, sam_file, output_file,qname_pickle,used_Cr):
    read_len = 151
    Cr = used_Cr
    fw = open(output_file,"w")
    f = open(h5_file,"r")
    mole_dict = defaultdict(list)
    droplet_dict = defaultdict(list)
    count_mole = 1
    for line in f:
        data = line.rsplit()
        """ start, end, length, barcode """
        mole_dict[count_mole] = [(int(data[1]),int(data[2]),int(data[3]),data[5])]
        droplet_dict[data[5]].append([(int(data[1]),int(data[2]),int(data[3]))])
        count_mole += 1
    print(len(droplet_dict))
    f.close()
    f = open(sam_file,"r")
    droplet_raw = defaultdict(list)
    curr = 0
    for line in f:
        #print(curr)
        curr += 1
        data = line.rsplit()
        qname = data[0]
        locus = int(data[3])
        barcode_field = [s for s in data if "BX:Z:" in s]
        barcode =  barcode_field[0].split(":")[2].split("-")[0]
        droplet_raw[barcode].append([qname,locus])

    
    count_mole = 1
    print(len(droplet_raw))
    count_zhou = 0
    for barcode, _qname_locus_list in droplet_raw.items():
        num_mole = len(droplet_dict[barcode])
        mole_start = []
        mole_end = []
        mole_len = []
        mole_qname = defaultdict(lambda: defaultdict(int))
        if num_mole > 0 :
            for i in range(num_mole):
                mole_start.append(droplet_dict[barcode][i][0][0])
                mole_end.append(droplet_dict[barcode][i][0][1])
                mole_len.append(droplet_dict[barcode][i][0][2])
            for i in range(len(_qname_locus_list)):
                qname = _qname_locus_list[i][0]
                locus = _qname_locus_list[i][1]
                for j in range(len(mole_start)):
                    start = mole_start[j]
                    end = mole_end[j]
                    if locus <= end and locus >= start:
                        mole_qname[(barcode,j)][qname] += 1
                        break

            for key, value in mole_qname.items():
                idx = key[1]
                length = mole_len[idx]
                choose_num = int(math.ceil(float(length*Cr)/(read_len*2)))
                if choose_num > 1:
                    total_qname_num = len(value.keys())
                    if total_qname_num > 0:
                        print(str(count_mole))
                        choose_qname_list = value.keys()
                        for one_qname in choose_qname_list:
                            fw.writelines(one_qname + "\t" + barcode +  "\n")
                    count_mole += 1

    read_qname_barcode_dict(output_file,qname_pickle)
    fw.close()
        
        
if __name__ == "__main__":
    chr_h5 = sys.argv[1]
    chr_sam_file = sys.argv[2]
    qname_file = sys.argv[3]
    qname_pickle = sys.argv[4]
    used_Cr = float(sys.argv[5])
    Extract_qname(chr_h5,chr_sam_file,qname_file,qname_pickle,used_Cr)
