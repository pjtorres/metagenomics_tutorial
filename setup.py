__author__ = 'Pedro J. Torres'
import subprocess
import os,re
import sys
import string

# python setup.py
# Script prepares your current environemnt for the metagenomics_tutorial found in
# https://github.com/pjtorres/metagenomics_tutorial

#------ check to make sure you are in the right directory ----------------------------
cwd=os.getcwd()
wd=cwd.split('/')[-1]
if wd != 'metagenomics_tutorial':
    print('You are not in the "metagenomics_tutorial" directory. Change to that directory then re-run this script.')
    exit(1)

#--------- check to make sure you have docker installed and working--------------------------
x=subprocess.Popen("docker -v",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=x.communicate()

if re.search('Docker version', output):
    print('Docker is properly installed.')
else:
    print('Docker is not installed or is not being called by your environment. Fix this then retry this script.')

#-------------- Set up fastp environment ---------------------------------------
print('Building fastp docker image')
meta='docker build -t metagenomics .'
subprocess.call(meta, shell=True)
meta='mkdir 1_QC'
subprocess.call(meta, shell=True)

#------------- Set up bowtie2 environment ----------------------------------------------
print('Pulling bowtie2 docker image')
bt2='docker pull biocontainers/bowtie2:v2.2.9_cv2'
subprocess.call(bt2, shell=True)

#-------- Set up samtools environment -------------------------------------------
print('Pulling samtools docker image')
sam='docker pull biocontainers/samtools:v1.2_cv3'
subprocess.call(sam, shell=True)

#---------- Set up bedtools environment --------------------------------------------
print('Pulling bedtools docker image')
bedtools='docker pull biocontainers/bedtools:v2.25.0_cv3'
subprocess.call(bedtools, shell=True)

#-------------- get human reference database and start organizing everything ----------------
print('Making refdb and downloading small human fna')
ref='mkdir refdb'
subprocess.call(ref, shell=True)
ref='mkdir 2_Decontam'
subprocess.call(ref, shell=True)

wget="docker run -v `pwd`:`pwd` -w `pwd` metagenomics wget ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/chr19.fa.gz"
subprocess.call(wget, shell=True)
ref='mv chr19.fa.gz refdb/'
subprocess.call(ref, shell=True)
ref="docker run -v `pwd`:`pwd` -w `pwd` metagenomics gunzip refdb/chr19.fa.gz"
subprocess.call(ref, shell=True)

#------------- set up metaphlan2  --------------------------------------------------------
print('Setting up metaphlan2 environment')
metaphlan2='docker pull qhmu/metaphlan2'
subprocess.call(metaphlan2, shell=True)
metaphlan2='mkdir metaphlan2'
subprocess.call(metaphlan2, shell=True)
metaphlan2='mkdir 3_Taxa/'
subprocess.call(metaphlan2, shell=True)



print('Set up done successfully! :)')
print('Before starting the tutorial go start downloading the metaphlan reference database from https://drive.google.com/drive/u/0/folders/1eWR6tgUoAUNXWsFujyLU5VNUzNMfxhDm  ')
print('Ready to start the metagenomics tutorial! :)')
