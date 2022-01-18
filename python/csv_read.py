import csv

csv_file = open("csv_write.csv", 'r', encoding='utf-8')

with csv_file:
    read_csv = csv.reader(csv_file)
    for row in read_csv:
        print(row)