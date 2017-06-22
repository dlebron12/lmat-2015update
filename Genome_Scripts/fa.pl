#!/bin/perl
use strict;

my $file = $ARGV[0];
my $dir = "$file.dir";

open(my $fh, '< :encoding(UTF-8)',$file) or die "Could not open file 'filename' $!";

if(-e $dir){
  chdir $dir; 
}else{mkdir $dir; chdir $dir;} 

my $f="vnf"; open(my $ch, '>>',$f);
while( my $row = <$fh>)
{    
       chomp $row;  
        if ($row =~ m/sequence_id\s(\d+)/){
  	   if(!-e $1){ print{$ch} "$1\n";      
           mkdir "$1", 0770; chdir "$1/";} else{chdir "$1";}   
           my $seq=<$fh>; 
           my $filename = "$1.fa";
        
        open(my $sf,'>',$filename)|| "file not created\n" ;
        print {$sf} $seq."\n"; close $sf;        
       } else{
           print "parse error, fix $row\n";

          } 
        chdir "../"; 
  }
close P;   
