
f = open("file.tab","rb")
for line in f:
    row = line.split()
    if row[2] > 40 and row[3] < 100:
        print line


