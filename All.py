'''import csv
import psycopg2

conn_string = "dbname= 'election' user = 'postgres' password = 'password'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

reader = csv.reader(open('american-electin-tweets.csv'.'rb'))

for row in reader:
    print row [1]

    statement = "INSERT INTO product_template (handle,tweet, "
'''

from One import func1
from Two import func2
from Three import func3
from Four import func4

def main():
    func4()
    func1()
    func2()
    func3()

if __name__=='__main__':
    main()
