#! /bin/bash
cd /home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno

tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 3 | sed 's/chr1//g' > ucsc.hg19.chr1.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 4 | sed 's/chr2//g' > ucsc.hg19.chr2.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 5 | sed 's/chr3//g' > ucsc.hg19.chr3.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 6 | sed 's/chr4//g' > ucsc.hg19.chr4.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 7 | sed 's/chr5//g' > ucsc.hg19.chr5.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 8 | sed 's/chr6//g' > ucsc.hg19.chr6.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 9 | sed 's/chr7//g' > ucsc.hg19.chr7.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 10 | sed 's/chr8//g' > ucsc.hg19.chr8.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 11 | sed 's/chr9//g' > ucsc.hg19.chr9.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 12 | sed 's/chr10//g' > ucsc.hg19.chr10.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 13 | sed 's/chr11//g' > ucsc.hg19.chr11.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 14 | sed 's/chr12//g' > ucsc.hg19.chr12.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 15 | sed 's/chr13//g' > ucsc.hg19.chr13.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 16 | sed 's/chr14//g' > ucsc.hg19.chr14.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 17 | sed 's/chr15//g' > ucsc.hg19.chr15.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 18 | sed 's/chr16//g' > ucsc.hg19.chr16.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 19 | sed 's/chr17//g' > ucsc.hg19.chr17.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 20 | sed 's/chr18//g' > ucsc.hg19.chr18.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 21 | sed 's/chr19//g' > ucsc.hg19.chr19.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 22 | sed 's/chr20//g' > ucsc.hg19.chr20.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 23 | sed 's/chr21//g' > ucsc.hg19.chr21.txt
tr -d '\n' < ucsc.hg19.fasta | cut -d '>' -f 24 | sed 's/chr22//g' > ucsc.hg19.chr22.txt
