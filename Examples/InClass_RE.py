import re

DNA = [ "AGGGATAGCGGAGTGACCC",
        "AGGGATAGTGGAGTGACCC",
        "AGGGATAGT--GAGTGACCC",
        "AGGGATAGT-GAGTGACCC" ]
for dna in DNA:
    m = re.search("G([CT]-{0,2}G)", dna)
    if m:
        print "dna string", dna, "had a match. It was", m.group(0), m.group(1)
        
        
# find stop codons

CODING = "ATGGGTAATTAT"
m = re.search("(TA[AG]|TGA)$",CODING)
if m:
    print "matched ", m.group(0)
else:
    print "no stop codon at end"
