import sys

def process_fastqs_file(input_R1,input_R2,output_RA,output_IA):
    f_R1 = open(input_R1,"r")
    f_R2 = open(input_R2,"r")
    f_RA = open(output_RA,"w")
    f_IA = open(output_IA,"w")
    count = 0
    temp = [] 
    curr = 0
    for line1, line2 in zip(f_R1,f_R2):
        print(curr)
        curr += 1
        if count%4 == 0:
            data1 = line1.rsplit()
            data2 = line2.rsplit()
            line1_idx = line1.split()[0] + "\t" + "1:N:0" + "\n"
            line2_idx = line2.split()[0] + "\t" + "2:N:0" + "\n"
            f_RA.writelines(line1_idx)
            barcode = line1.split()[1].split(":")[-1] + "\n"
            temp.append(line2_idx)
            count += 1
        else:
            f_RA.writelines(line1)
            temp.append(line2)
            count += 1

        count_read = 0

        if len(temp) == 4:
            for read in temp:
                if count_read == 0:
                    f_IA.writelines(read)
                f_RA.writelines(read)
                count_read += 1
            f_IA.writelines(barcode)
            f_IA.writelines("+" + "\n")
            f_IA.writelines("AAFFFKKK" + "\n")

            temp = []

if __name__ == "__main__":
    R1_file = sys.argv[1]
    R2_file = sys.argv[2]
    output_RA= sys.argv[3]
    output_I1 = sys.argv[4]
    process_fastqs_file(R1_file,R2_file,output_RA,output_I1)
