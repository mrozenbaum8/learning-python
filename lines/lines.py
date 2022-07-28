import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith('.py') == False:
    sys.exit("Not a Python file")

counter = 0

with open(sys.argv[1], "r") as file:
    reader = file.readlines()
    for line in reader:
        if "#" in line:
            counter += 0
        elif len(line.strip()) == 0:
            counter += 0
        else:
            counter += 1
print(counter)