lens<- read.table("polyA_lengths.dat")
pdf("polyA_lengths_histogram.pdf")
hist(lens$V1,100,main="PolyA Lengths",xlab="Length (bp)")
