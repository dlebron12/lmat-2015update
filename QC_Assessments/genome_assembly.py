#! /usr/tce/bin/ipython 

# Outputs full fasta
def Readfile(fileName):
    with open(fileName) as f:
        return filter(None,[line.rstrip("\n") for line in f if not line.startswith(">")])

def Assemble_genome(left, right):
    #Overlap #
    #computes overlap between two fragments
    for i in range(len(left)):
        if left[i:] == right[:len(left)-i]:
            #there is an overlap here: left[i:]
            return left[0:i-1]+left[i:]+right[len(left)-i:]
    #if overlap doesnt exist add N's
    return ''

def get_genome(reads):
    genome=reads[0]
    for i in range(1,len(reads)):
        #Build genome recursively
        genome=Assemble_genome(genome,reads[i])
    return genome

#IMPORTS
import re
import sys
import os


if __name__== "__main__":
    header_file=sys.argv[1] # input the header_file
    header_file=header_file.rstrip("\n")
    wd='/usr/mic/post1/metagenomics/ref_sets/fasta/01012015update/sinceMar2014'#depending the header file we do the wd
    match=re.search('^(.*?).headers$',header_file)
    folder=match.group(1) #name of the directory to look out for the sequences
    with open(header_file) as hf:
        #change folder
        folder_dir=folder+".dir"
        os.chdir(folder_dir)
        g=open(folder+".big_fasta.txt","a")
        for header in hf:
        #get seqid using re
            match=re.search('\[sequence_id (\d+)\]',header)
            seqid=match.group(1)
            os.chdir(seqid)
            if seqid+"_v2.fa.frag" in os.listdir("."):
                reads = Readfile(seqid+"_v2.fa.frag")
                genome=reads[0]
                #Ensemble genome from frag fasta file.
                for i in range(1,len(reads)):
                    genome=Assemble_genome(genome,reads[i])
            else:
                #Nothing was taken from fasta file so just take original fasta
                genome=Readfile(seqid+".fa")[0]
        #open a new txt file giant_fasta and append header and genome information in

            g.write(header+"\n")
            g.write(genome+"\n")
            os.chdir('..')
    hf.close()
    g.close()
