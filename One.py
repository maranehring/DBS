import unicodecsv
def func1():
    with open('american-election-tweets.csv','r') as inp, open('first_file.csv', 'w') as out:
        writer = unicodecsv.writer(out, delimiter=';', lineterminator='\n', encoding='ISO-8859-1')
        stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')

        all = []
        row = next(stuff)
        row.append('hasHashtag')
        all.append(row)
        #Fuege neue Spalte hinzu

        for row in stuff:
            if row[10]=="False": #Falls Tweet nicht abgekuerzt wurde
                if "#" in row[1]: #Falls Tweet Hashtag benutzt
                    row.append("True") #Schreibe "True" in neue Spalte
                    #writer.writerow(row) #Schreibe Zeile in neues Dokument
                else:
                    row.append("False") #Schreibe "False" in neue Spalte
                    #writer.writerow(row) #Schreibe Zeile in neues Dokument
                all.append(row)
        writer.writerows(all)
