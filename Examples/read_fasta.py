import itertools
import gzip
import sys
import re

# based on post here
# https://drj11.wordpress.com/2010/02/22/python-getting-fasta-with-itertools-groupby/

# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

# this function reads in fasta file and returns pairs of data
# where the first item is the ID and the second is the sequence
# it isn't that efficient as it reads it all into memory
# but this is good enough for our project
def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = group.next()
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence
        
# here is my program
# get the filename from the cmdline

filename = sys.argv[1]


if re.match('(\S+)\.gz$',filename):
    with gzip.open(filename,"rb") as f:
        seqs = dict(aspairs(f))        
else:
    print "filename ",filename,"doesn't match .gz"
    with open(filename,"r") as f:
        seqs = dict(aspairs(f))        

n=0
for k,v in seqs.iteritems():
    print "id is ",k,"seq is",v
    n += 1

print n,"sequences"
