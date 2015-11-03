Homework 5
==========

Due Nov 11

1. Write a script using the 'csv' package to parse [this _E.coli_ vs
_Salmonella enterica_ BLAST
report](http://hyphaltip.github.io/GEN220_2015/data/Ecoli-vs-Senterica.BLASTP.tab.gz) and [this _E.coli_ vs _Yersinia pestis_ BLAST report](http://hyphaltip.github.io/GEN220_2015/data/Ecoli-vs-Yersinia.BLASTP.tab.gz) 
and make a new report which prints out the _E.coli_ sequence ID, and a column for the best _Salmonella_ hit and the best _Yersinia_ hit.
best hit for each sequence to a file call 'Ecoli_report.tab'.
Also print to STDOUT a summary report with the total number of
sequences with a good hit in _E.coli_ to each Salmonella and Yersina (e.g. 1000 proteins in Ecoli had a Salmonella hit, 700 had a hit to Yersinia).
  Screen the search results - don't take a best hit if something is less
than 40% identical at the protein level.

2. Using BioPython SeqIO module and any others you need, write a script to parse [the transcript
sequences](https://www.vectorbase.org/download/ixodes-scapularis-wikeltranscriptsiscaw14fagz)
from the Tick _Ixodes scapularis_ genome and print out.

* the max, minimum, and average length of these transcripts.
* Number of transcripts which start with ATG
* GC content of the transcripts
