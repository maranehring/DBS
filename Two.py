import unicodecsv
def func2():
    with open('first_file.csv','r') as inp, open('second_file.csv', 'w') as out:
        writer = unicodecsv.writer(out, delimiter=';', lineterminator='\n', encoding='ISO-8859-1')
        stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')

        lines = [l for l in stuff]
        i = 0
        for row in lines:
            if row[0] == "HillaryClinton": #Falls die erste Spalte HillaryClinton ist,
                lines[i][0] = "True" #benenne sie um in "True"
            else:
                lines[i][0] = "False" #Sonst benenne sie um in "False"

            i = i + 1
        writer.writerows(lines)

