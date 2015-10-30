import sys
#import Bio
from Bio import SeqIO
from Bio.Seq import Seq

# seqfile is data/AJ240084_TRIM.gbk
filename = sys.argv[1] 
for seq_record in SeqIO.parse( filename , "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print seq_record.seq
    print(len(seq_record))

