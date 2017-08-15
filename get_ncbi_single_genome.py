#!/usr/local/bin/python

#NOTE: PLEASE RUN THIS IN THE DIRECTORY WERE YOU WANT THE DOWNLOADS TO BE

##Please refer to confluence entrance:
#  https://lc.llnl.gov/confluence/x/JQD6FQ

##Example list of accessions can be found here:
# /data04/kpath/downloader/ncbi_update/ncbi_update.assembly

### IMPORTS
import ftplib
import os,sys
import time
import pandas as pd
import gzip

###Variables for job submission####

def getFile(ftp,fasta):
    #downloadDir= os.getcwd()
    downloadDir="/home/lebronaldea1/genbank_2017/ncbi_update"
    local_fasta=os.path.join(downloadDir,fasta)
    size=os.path.getsize(local_fasta)

    #If file does not exist or if it exist but size is 0
    if local_fasta.exists() == False or size != 0:
        fhandle=open(local_fasta,'wb')
    #print 'Getting '+ fasta_file[0]
        ftp.retrbinary('RETR '+ fasta, fhandle.write)
        fhandle.close()
    else:
        pass

def SortFiles.Date(dir_ls):
    for i in dir_ls:

        #Check is a DIRECTORY
        #Check what the creation date is
        #Rearrange list by creation Date (pair-wise comparison)

        #Compare two dates
        date1 = "31/12/2015"
        date2 = "01/01/2016"
        newdate1 = time.strptime(date1, "%d/%m/%Y")
        newdate2 = time.strptime(date2, "%d/%m/%Y")
        newdate1 < newdate2 #True


    return sorted_ls[0] #newest

#############################CODE#############################
# Input is accession to download
# Output is the fasta download

#file=sys.argv[0]
#file='ncbi_update.assembly'
 #second column is the accession number
#file_df= pd.read_table(os.path.join(downloadDir,file),header=None)
#file_ls=file_df[1].tolist()

#Open ftp
link='ftp.ncbi.nih.gov'
user='anonymous'
email='lebronaldea1@llnl.gov'
ftp=ftplib.FTP(link,timeout=None)
ftp.login(user,email)
#for each accession, divide the accession and create wd

#accession=file_ls[0]
accession=sys.argv[0]
#for accession in file_ls:
spl=accession.split("_")
Dir='/genomes/all/'+spl[0] #GCA folder or other
projectID=spl[1].split(".")[0] #projectID.1
#The folders are divided by splitting full project ID in 3 digits
f1,f2,f3=projectID[:3],projectID[3:6],projectID[6:9]
### Search fasta files in directory and check creation dates
fastaDir=os.path.join(Dir,f1,f2,f3)
ftp.cwd(fastaDir)
versions=ftp.nlst(".")

#Choose the newest modified version
if len(versions)==1:
    f4=versions[0]
#there are more versions
else:
    print accession + " has multiple directories\n"
    f4=SortFiles.Date(versions) #gets recent verison

ftp.cwd(f4)
files=ftp.nlst(".")
fasta_file=[i for i in files if re.search('v1_genomic.fna.gz',i)][0]
getFile(ftp,fasta_file)

ftp.quit()
