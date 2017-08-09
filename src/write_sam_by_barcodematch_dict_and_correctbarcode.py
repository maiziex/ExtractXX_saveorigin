#import pdb
#pdb.set_trace()
from collections import defaultdict
import sys

def write_new_sam_by_barcode_dict(whitelist_fa,barcode_sam_file,sam_file,output_file):
    f = open(whitelist_fa,"r")
    count = 0
    whitelist_dict = defaultdict()
    for line in f:
        data = line.rsplit()
        if count%2 == 0:
            idx = int(data[0].split(">")[1])
        elif count%2 == 1:
            whitelist_dict[idx] = data[0]
        count += 1

    f.close()
    f = open(barcode_sam_file,"r")
    barcode_qname_dict = defaultdict(list)
    for line in f:
        data = line.rsplit()
        if data[0][0] == "@":
            continue
        else:
            qname = data[0]
            cigar = data[5]
            try:
                ref_barcode_idx = int(data[2])
                if cigar == "16M" or cigar == "15M1S" or cigar == "1S15M" or cigar == "14M2S" or cigar == "2S14M":
                    barcode = whitelist_dict[ref_barcode_idx]
                    barcode_qname_dict[qname] = [barcode]
            except:
                print(data[2])
    f.close()

    f = open(sam_file,"r")
    fw = open(output_file,"w")

    for line in f:
        data = line.rsplit()
        qname = data[0]
        if len(barcode_qname_dict[qname]) == 1:
            barcode  = barcode_qname_dict[qname][0]
            data[-1] = "BX:Z:" + barcode + "-1\n"
            fw.writelines('\t'.join(data))

    f.close()
    fw.close()


#write_new_sam_by_barcode_dict("chr2_barcode.sam","chr2.sam","chr2_filter_bybarcode.sam")
if __name__ == "__main__":
    whitelist_fa = sys.argv[1]
    chr_barcode_sam_file = sys.argv[2]
    chr_sam_file = sys.argv[3]
    new_sam_file = sys.argv[4]
    write_new_sam_by_barcode_dict(whitelist_fa,chr_barcode_sam_file,chr_sam_file,new_sam_file)
