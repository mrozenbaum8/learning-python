s = input("camelCase: ")

for c in s:
    if c.isupper():
        c = c.lower()
        print(f"_{c}", end="")
    else:
        print(c, end="")
print()