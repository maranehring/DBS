import unicodecsv
def func3():
    with open('second_file.csv', 'r') as inp, open('third_file.csv', 'w') as out:
        writer = unicodecsv.writer(out, delimiter=';', lineterminator='\n', encoding='ISO-8859-1')
        stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')
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
            special='' #Mache "special" wieder leer für die naechste Iteration
            j += 1
        writer.writerows(lines)
