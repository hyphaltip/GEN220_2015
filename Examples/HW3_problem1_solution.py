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
# one way to solve this
#length = len dna;
length = 0

# New code here
for base in dna:
    length += 1
    if base == "C": 
        GC += 1
    elif base == "G":
        GC += 1
# rewrite this as
#if base == "C" or base == "G":
        
print "GC content for dna string is ", (100.0 * GC)/length;
print "length of string is ", length;

# identify the location of all the ATG
atg_codons = [];

# your code here

query = "ATG"
start = 0
atg = dna.find(query,start)
while atg >= 0:    
    atg_codons.append(atg)
    #print "atg is at ", atg    
    start = atg + len(query)
    atg = dna.find(query,start)
    

print "The position of the ATG codons is :";
for codon in atg_codons:
    print "ATG at position ", codon;


# print the reverse complement

revcom = "";

for n in range(len(dna)-1,-1, -1):
    base = dna[n]
    if base == "A":
        revcom += "T"
    elif base == "T":
        revcom += "A"
    elif base == "C":
        revcom += "G"
    elif base == "G":
        revcom += "C"

# your code here

print "The DNA string is: ";
print dna;
print "The reverse complement of DNA string is: ";
print revcom;




