x, y, z = input("Expression: ").split(" ")
x = float(x)
z = float(z)

if y == "+":
    r = x + z
elif y == "-":
    r = x - z
elif y == "*":
    r = x * z
elif y == "/":
    r = x / z

print(f"{r}")