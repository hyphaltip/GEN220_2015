
# I ran this first
# bedtools intersect -wa -a data/Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3 -b data/rice_chr6_3kSNPs_filt.bed | grep "\tgene\t" | cut -f4,5,9 | sort | uniq -c > genes_with_snps.count
# I don't care about what the specific SNPs are so I use
# -wa option to write out the original gene feature
# I only want the gene features, so I use grep "\tgene\t" to get thise
# -- its possible this may not work on some unix - you can try
# grep -P "\tgene\t" to support extended pattern search 
# I use cut -f4,5,9 to get the start,end, and group name for the gene
# I use sort and uniq -c to collapse redundant ones into a single line with
# a count

# print our report header
# some code to print the list with "\t" separating the input
print ("\t".join([str(x) for x in ("gene_name","length","SNP","SNPs_per_kb")]))
# also could write as
#print ("gene_name"+"\t"+"length"+"\t"+"SNP"+"\t"+"SNPs_per_kb");


counts = open("genes_with_snps.count","r")
gene_count_dict = {}
dat = []
for geneline in counts:
    row = geneline.split()
    #most of the info we need is in the BEDtools output
    snp_count = int(row[0]) # goint to use this as a number later
    gene_start = int(row[1]) # going to use this as a number later
    gene_end   = int(row[2]) # going to use this as a number later
    gene_group = row[3]

    # compute the gene length from the start and end columns
    # add one because feature start at 1 and are inclusive in GFF
    # e.g. a feature going from 10..11 is length 2 so
    # 11-10 = 1; need to add 1 to make it 2
    gene_len = gene_end - gene_start + 1
    # use these bits to cut out the gene name (regular expression would
    # work too)
    ids = gene_group.split(":")
    genestuff = ids[1].split(";")
    gene_name = genestuff[0]
    # print it all out
    SNP_ratio =  (1000.0 * snp_count / gene_len) # mult by 1000 to get it in SNPs / kb
    # some code to print the list with "\t" separating the input
    dat.append([gene_name, gene_len, snp_count,SNP_ratio])

# sort by the 4th column (eg col[3]), largest to smallest so we use reverse=True
dat.sort(key=lambda col: int(col[3]),reverse=True)

for result in dat:
        print ("\t".join([str(x) for x in result]))

