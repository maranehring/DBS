import csv
def func2():
    with open('newfile.csv','r') as inp, open('first_edit.csv', 'w') as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        stuff = csv.reader(inp, delimiter=';')

        lines = [l for l in stuff]
        i = 0
        for row in lines:
            if row[0] == "HillaryClinton": #Falls die erste Spalte HillaryClinton ist,
                lines[i][0] = "True" #benenne sie um in "True"
            else:
                lines[i][0] = "False" #Sonst benenne sie um in "False"

            i = i + 1
        writer.writerows(lines)


