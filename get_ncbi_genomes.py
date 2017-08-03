### IMPORTS
import ftplib
import os,sys
from more-itertools import sliced
from time import sleep
import pandas as pd

###Variables for job submission####
sleepTime=5
batchSize=100

###Method###
def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print "Error"

##### Input is list of accessions to download
##Please refer to confluence entrance:
##Example list of accessions can be found here:

file=sys.argv[0]
file_ls=pd.read_table(file,header=False)[1] #second column is the accession number

#Open ftp
link='ftp://ftp.ncbi.nlm.ncbi.nih.gov'
user='anonymous'
email='lebronaldea1@llnl.gov'
ftp=ftplib.FTP(link)
ftp.login(user,email))
#for each accession, divide the accession and create wd

for accession in file_ls:
    acc.spl=accession.split("_")
    Dir='/genomes/all/'+acc.spl[0]
    projectID=acc.spl[1]
    fastaDir=os.path.join(*list(sliced(projectID,3)))
    ### Search fasta files in directory
    fastaFile=os.path.join(Dir,fastaDir)
    #get fasta file
    getFile(ftp,fastaFile)

ftp.quit()
