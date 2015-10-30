


for row in file:
    line = row.split("\t")
    key = line[3]
    value = line[6]
    localization[key] = value
