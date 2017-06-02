import csv
def func3():
    with open('first_edit.csv', 'r') as inp, open('finalFile.csv', 'w') as out:
        writer = csv.writer(out, delimiter=';', lineterminator='\n')
        stuff = csv.reader(inp, delimiter=';')
        special = ''
        lines = [l for l in stuff]
        j=0
        for line in lines:
            for i in line[4]:
                x=i.strip(':') #Entferne ":" aus der "Zeit"-Spalte
                y=x.strip('-') #Entferne "-" aus der "Zeit"-Spalte
                z=y.strip('T') #Entferne "T" aus der "Zeit"-Spalte
                special+=z 
            lines[j][4] = special #Definiere die "Zeit"-Spalte als special
            special='' #Mache "special" wieder leer für die nächste Iteration
            j += 1
        writer.writerows(lines)
