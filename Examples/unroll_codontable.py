
with open("data/codon_table_compact.txt","r") as f:
    for n in f:
        row = n.split()
        for c in row[0].split(","):
            print "\t".join([c,row[1],row[2]])
