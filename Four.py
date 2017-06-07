import unicodecsv
def func4():
    with open('third_file.csv', 'r') as inp, open('last_file.csv', 'w') as out:
        writer = unicodecsv.writer(out, delimiter=';', lineterminator='\n', encoding='ISO-8859-1')
        stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')

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
