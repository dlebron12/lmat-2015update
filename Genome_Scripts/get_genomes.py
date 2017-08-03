### IMPORTS
import ftplib
import os,sys

##### Input is list of accessions to download
##Please refer to confluence entrance:
##Example list of accessions can be found here:

file=sys.argv[0]

#Open ftp
link=
user='anonymous'
email='lebronaldea1@llnl.gov'
ftp=ftplib.FTP(link,user,email)
#for each accession, divide the accession and create wd

for accession in file_ls:
    cd=
    ftp.cwd(cd)
    fasta_file=
    ftp.get()
