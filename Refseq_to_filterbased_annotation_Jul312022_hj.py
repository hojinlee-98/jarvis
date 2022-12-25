### 20220730 ###

## python3.7
## Refseq_to_filterbased_annotation_Jul312022_hj.py

import numpy as np
import sys

### usage ###
# python Refseq_to_annovarformat.py [path/inputfile] [path/inputfile2] [path/outputfile] [chr1]
if len(sys.argv) != 5:
    print("please, check input files")
else:
    input_file = sys.argv[1]  # string
    input_file2 = sys.argv[2]  # string
    output_file = sys.argv[3]  # string
    chrom_numb = sys.argv[4]  # string


class RefSeqExtension:
    def __init__(self, input_file, input_file2, output_file, chrom_numb):
        self.input_file = input_file
        self.input_file2 = input_file2
        self.output_file = output_file
        self.chrom_numb = chrom_numb
        self.chrom = []
        self.pos = []
        self.ref = []
        self.alt = []
        self.jarvis = {}

    ### openfasta ###
    # read ucsc fasta file
    def openfasta(self):
        file1 = open(self.input_file, "rt")
        fasta = file1.read()
        fasta = fasta.upper()  # change lower to upper
        return fasta

    ### openjarvis ###
    # it is better to use a dictionary when inserting, deleting, or searching elements.
    def openjarvis(self):
        with open(input_file2) as file2:
            while True:
                aline = file2.readline().strip()
                if not aline:
                    break
                jarvis_pos = int(aline.split("\t")[1])
                jarvis_score = float(aline.split("\t")[3])
                self.jarvis[jarvis_pos] = jarvis_score
        return

    ### PosRefChrom_extension ###
    # called by Alt_extension
    def PosRefChrom_extension(self, i, v):
        self.pos.extend([i + 1, i + 1, i + 1])  # python index is started at zero. (position = index + 1)
        self.ref.extend([v, v, v])
        self.chrom.extend([self.chrom_numb, self.chrom_numb, self.chrom_numb])
        return

    ### Alt_extension ###
    # check out reference sequences
    # and if there is no "N" , extend the alt alleles.
    def Alt_extension(self, i, v):
        if v == "N":
            return False
        elif v == "A":
            self.PosRefChrom_extension(i, v)
            self.alt.extend(["G", "C", "T"])
        elif v == "G":
            self.PosRefChrom_extension(i, v)
            self.alt.extend(["A", "C", "T"])
        elif v == "C":
            self.PosRefChrom_extension(i, v)
            self.alt.extend(["A", "G", "T"])
        elif v == "T":
            self.PosRefChrom_extension(i, v)
            self.alt.extend(["A", "G", "C"])
        return True

    def main_function(self):
        fasta = self.openfasta()
        self.openjarvis()

        with open(self.output_file, 'w') as file3:
            for i, v in enumerate(fasta):
                self.chrom = []
                self.pos = []
                self.ref = []
                self.alt = []
                if self.jarvis.get(i+1): # if jarvis dict has the key(i+1), return True
                    TF = self.Alt_extension(i, v)
                    if TF == True:
                        score = self.jarvis[i + 1]
                        ar = np.array([self.chrom, self.pos, self.ref, self.alt])
                        #print(ar)
                        ar = ar.T
                        file3.write(ar[0,0] + '\t' + ar[0,1] + '\t' + ar[0,1] +
                                    '\t' + ar[0,2] + '\t' + ar[0,3] + '\t' + f"{score}\n")
                        file3.write(ar[1,0] + '\t' + ar[1,1] + '\t' + ar[1,1] +
                                    '\t' + ar[1,2] + '\t' + ar[1,3] + '\t' + f"{score}\n")
                        file3.write(ar[2,0] + '\t' + ar[2,1] + '\t' + ar[2,1] +
                                    '\t' + ar[2,2] + '\t' + ar[2,3] + '\t' + f"{score}\n")
                    else :
                        continue
                else:
                    continue

my_obj = RefSeqExtension(input_file, input_file2, output_file, chrom_numb)
my_obj.main_function()
