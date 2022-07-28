import sys
import PIL

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].lower().endswith('.jpg') == False and sys.argv[1].lower().endswith('.jpeg') == False and (sys.argv[1]).lower().endswith('.png') == False:
    sys.exit("Invalid input")

elif sys.argv[2].lower().endswith('.jpg') == False and sys.argv[2].lower().endswith('.jpeg') == False and (sys.argv[2]).lower().endswith('.png') == False:
    sys.exit("Invalid input")

elif sys.argv[2].lower().endswith() != sys.argv[1].lower().endswith():
    sys.exit("Invalid input")

input = []
output = []

try:
    with open(sys.argv[1], 'r') as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            input.append(row)
except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)

