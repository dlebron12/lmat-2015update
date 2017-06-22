#! /bin/sh 
#Run LMAT for each of the genome sequences

for i in $(cat dir.ls );do
  cd "$i";
  #EXCHANGE FOR ACTUAL RS.SH SCRIPT.
  /g/g19/bioinf/rs_dla.sh "$i".fa.frag;
  cd ../
done  
 
    
