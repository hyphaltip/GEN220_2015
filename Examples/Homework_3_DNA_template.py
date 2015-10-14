# This is Python code
# this is a template for answering homework #3

# dna string
dna = ('ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGA'
       'GGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGC'
       'AGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATG'
       'CTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGC'
       'TCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGAT'
       'CCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCA'
       'CCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCA'
       'CTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACT'
       'GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGC')

print "dna is " + dna


# compute the % of G+C bases in the DNA string (e.g. the GC content)

GC = 0;
length = 0;
# your code here


print "GC content for dna string is " + GC;
print "length of string is " + length;

# identify the location of all

atg_codons = [];

# your code here


print "The position of the ATG codons is :";
for codon in atg_codons:
    print "ATG at position " + codon;


# print the reverse complement

revcom = "";


# your code here

print "The DNA string is: ";
print dna;
print "The reverse complement of DNA string is: ";
print revcom;




