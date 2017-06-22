#!/bin/perl

#This script checks if the fastsummary for the genome was done and if not it resubmits the job.
my $directory=$ARGV[0];
my $catalog = $ARGV[1];
open(my $sh,'<', $catalog)|| die "Couldnt open catalog";
chdir $directory;
while(my $catline=<$sh>){  
   
    chomp $catline;
    my @info= split /\t/, $catline;
    my $taxid=$info[3];
   
    my $seqid=$info[1];
my $fast="$seqid/data.$seqid.fa.frag/$seqid.fa.frag.cleaned.db.lo.rl_output.0.30.fastsummary";
if(! -f $fast){
 print "$seqid\n";chdir $seqid;system("/g/g19/bioinf/rs_dla.sh $seqid.fa.frag");chdir "../";}
 } close $sh;
