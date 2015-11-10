import warnings

# you should have downloaded and unzipped the file
# http://hyphaltip.github.io/GEN220_2015/data/Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz
# and have it in the current directory (or used a symlink or you can change this program) - will cover how to read gzipped data in directly later

# this code will open the file for reading. You shouldn't need to change it
gff3 = open("Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3","r")

# these are some variables you will need to update in the loop below
gene_count = 0;
CDS_count = 0;
num_gene_bases = 0;
num_CDS_bases = 0;
chrom_6_length = 31248787; # hardcode this for now - the length of Chr6

gene_feature_counts = {}
#  this loop will read the lines in the file one by one
for line in gff3:
    # this if statement will skip lines that start with a comment
    if line.find("#") == 0:
        # this will go to the next line in the file by going to
        # back to start of for loop
        continue 
    else:
        # use the split function to turn the line into a list
        row = line.split("\t");
        group = row[-1]
        if row[2] == "gene":
            gene_count += 1
            num_gene_bases += int(row[4]) - int(row[3])
        elif row[2] == "CDS":
            CDS_count += 1
            num_CDS_bases += int(row[4]) - int(row[3])


        # this part also counts number of exons per gene for extra credit
        # only process CDS and exon features next
        if row[2] != "CDS" and row[2] != "exon":
            continue
        
        groupid = ""
        
        for type in group.split(";"):
            kv = type.split("=",1)            
            keyval = { kv[0] : kv[1] }
            if "Parent" in keyval:
                groupid = keyval["Parent"]
            elif "ID" in keyval:
                groupid = keyval["ID"]
        # get rid of whitespace
        groupid = groupid.split()[0]
        
        if groupid == "":
            warnings.warn("no groupid parsed for line "+line)
            continue
        
        gn = gene_feature_counts.get(groupid,{})
        curval = gn.get(row[2],0)
        gn[row[2]] = curval+1
        gene_feature_counts[groupid] = gn
        
        
# end of for loop


CDS_fraction = float(num_CDS_bases) / chrom_6_length

print "There are {} genes" .format(gene_count);
print "There are {} exons" .format(CDS_count);
print "There are {} bases which are in genes out of {}".format(num_gene_bases,chrom_6_length);
print "There are {} bases which are in exons out of {}".format(num_CDS_bases,chrom_6_length);
print "%.2f%% of the Chr6 bases are coding" % (100*CDS_fraction);

for gene in gene_feature_counts.keys():    
    print "%s has %d exons and %d CDS" % (gene,gene_feature_counts[gene].get("exon",0),
                                          gene_feature_counts[gene].get("CDS",0))
