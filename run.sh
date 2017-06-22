#! /bin/sh 


for i in $(cat dir.ls );do
  cd "$i";
  /g/g19/bioinf/rs_dla.sh "$i".fa.frag;
  cd ../
done  
 
    
