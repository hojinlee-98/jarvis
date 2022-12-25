# jarvis
this repository includes scripts for making jarvis db that are calculated for pathogenicity of noncoding regions.
```shell
### 20220901 ###

### 1. 
[jc2545@c13n04 script]$ cat ucsc.hg19.fa_edit_20220730_hj.sh 
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

# split
[jc2545@c13n04 script]$ sh ucsc.hg19.fa_edit_20220730_hj.sh


### 2. make jarvis db splited by chromosome 
[jc2545@c16n10 script]$ dsq --job-file Refseq_to_filterbased_annotation_command.sh -J hj_jarvis -t 120:00:00 --mem=10G -c 1
Batch script generated. To submit your jobs, run:
 sbatch dsq-Refseq_to_filterbased_annotation_command-2022-09-02.sh
[jc2545@c16n10 script]$  sbatch dsq-Refseq_to_filterbased_annotation_command-2022-09-02.sh
Submitted batch job 15926233

### 2. random sampling
[jc2545@c16n10 hg19_jarvis]$ mkdir sanity_check
[jc2545@c16n10 hg19_jarvis]$ awk '{print "source ~/.bashrc; cd /home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno/annovarformat/hg19_jarvis; head -n 9 hg19_jarvis_chr"$1"_filterbased_annotation.txt > ./sanity_check/jarvis_sanity_check_head_chr"$1".txt"}' < chrom_seq.txt > sanity_check.sh
[jc2545@c16n10 hg19_jarvis]$ sh sanity_check.sh

[jc2545@c16n10 hg19_jarvis]$ awk '{print "source ~/.bashrc; cd /home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno/annovarformat/hg19_jarvis; tail -n 9 hg19_jarvis_chr"$1"_filterbased_annotation.txt > ./sanity_check/jarvis_sanity_check_tail_chr"$1".txt"}' < chrom_seq.txt > sanity_check_tail.sh
[jc2545@c16n10 hg19_jarvis]$ sh sanity_check_tail.sh

### 3. raw data head and tail
[jc2545@c16n10 editfile]$ awk '{print "source ~/.bashrc; cd /home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno/jarvis_paper/hg19/JARVIS/editfile; head -n 3 "$1" > head_"$1""}' < file_list.txt > jarvis_head.sh
[jc2545@c16n10 editfile]$ awk '{print "source ~/.bashrc; cd /home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno/jarvis_paper/hg19/JARVIS/editfile; tail -n 3 "$1" > tail_"$1""}' < file_list.txt > jarvis_tail.sh
[jc2545@c16n10 editfile]$ sh jarvis_head.sh
[jc2545@c16n10 editfile]$ sh jarvis_tail.sh

[jc2545@c16n10 editfile]$ mv head* ../../../../annovarformat/hg19_jarvis/sanity_check/.
[jc2545@c16n10 editfile]$ mv tail* ../../../../annovarformat/hg19_jarvis/sanity_check/.



### compress
[jc2545@c16n10 hg19_jarvis]$ pwd
/home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno/annovarformat/hg19_jarvis
[jc2545@c16n10 hg19_jarvis]$ awk '{print "source ~/.bashrc; cd /home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno/annovarformat/hg19_jarvis; bgzip hg19_jarvis_chr"$1"_filterbased_annotation.txt"}' < chrom_seq.txt > compress.sh

[jc2545@c16n10 hg19_jarvis]$ dsq --job-file compress.sh -t 48:00:00 -J hj_compress -c 1 --mem=100G
Batch script generated. To submit your jobs, run:
 sbatch dsq-compress-2022-09-02.sh
[jc2545@c16n10 hg19_jarvis]$  sbatch dsq-compress-2022-09-02.sh


### indexing for annovar annotation
[jc2545@c16n10 hg19_jarvis]$ pwd
/home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno/annovarformat/hg19_jarvis
[jc2545@c16n10 hg19_jarvis]$ cat indexing_mv.sh 
#! /bin/bash
#SBATCH --job-name=hj_indexing
#SBATCH --mem=100G
#SBATCH -c 20
#SBATCH -t 120:00:00

cd /home/jc2545/ref_data/h_sapiens/noncoding_scores/noncoding_anno/annovarformat/hg19_jarvis

zcat *.gz > hg19_jarvis.txt

rm -rf *.gz

/ycga-gpfs/scratch60/lifton/jc2545/scripts/index_annovar.pl hg19_jarvis.txt
