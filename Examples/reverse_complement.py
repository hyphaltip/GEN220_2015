complementDNA = { 'A':'T',
                'T':'A',
                'G':'C',
                'C':'G'}


def revcom(dna):
#    print "input dna is ",dna
    revcom =""
    for let in reversed(dna):
        revcom += complementDNA[ let ]
    return revcom


DNA = "AAGTAGA"

print "DNA    is",DNA
print "revcom is",revcom(DNA)
