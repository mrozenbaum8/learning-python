import inflect
import sys

#p = inflect.engine()
names = []

while True:
    try:
        n = input("Name: ")
        names.append(n)
    except EOFError:
        print()
        #output = p.join(names)
        print(f"Adieu, adieu, to {inflect.engine().join(names)}")
        sys.exit()