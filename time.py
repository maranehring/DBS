import unicodecsv

with open('last_file.csv', 'r') as inp, open('time.csv', 'w') as out:
    writer = unicodecsv.writer(out, delimiter=';', lineterminator='\n', encoding='ISO-8859-1')
    stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')
    row = next(stuff)
    row.append('TweetID')
    all.append(row)
    c1=[]
    c2=[]

    for row in stuff:
        time = row[2]
        for i in range (0,7):
            c1.append(time[i])
        for i in range (8,13):
            c2.append(time[i])
        writer.writerow()
