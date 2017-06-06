import csv
import unicodecsv as csv
def func4():
    with open('american-election-tweets.csv', 'r') as inp, open('first_file.csv', 'w') as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        stuff = csv.reader(inp, delimiter=';')

        all = []
        row = next(stuff)
        row.append('TweetID')
        all.append(row)
        #Fuege neue Spalte hinzu
        i=1

        for row in stuff:
                row.append(i) #Schreibe "i" in neue Spalte
                i=i+1
                all.append(row)
        writer.writerows(all)
