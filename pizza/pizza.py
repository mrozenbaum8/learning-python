import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith('.csv') == False:
    sys.exit("Not a .csv file")

elif sys.argv[2].endswith('.csv') == False:
    sys.exit("Not a .csv file")

output = []

with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for row in reader:
        output.append(row)

print(tabulate(output, headers="firstrow", tablefmt="grid"))