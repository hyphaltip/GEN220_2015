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
        # here is example of how print some of the columns
        # you'll want to comment this next line out when your program works
        print row[2], row[3], row[4]; 
        # your code here, remember to indendent the same

# end of for loop


CDS_fraction = 0; # update this to calc the fraction of the chromosome which is coding bases

print "There are {} genes" .format(gene_count);
print "There are {} exons" .format(CDS_count);
print "There are {} bases which are in genes out of {}".format(num_gene_bases,chrom_6_length);
print "There are {} bases which are in exons out of {}".format(num_CDS_bases,chrom_6_length);
print "{} % of the Chr6 bases are coding".format(100*CDS_fraction);

