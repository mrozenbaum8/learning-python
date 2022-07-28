n = 50

while n > 0:
    print(f"Ammount Due: {n}")
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        n = n - coin
n = n * -1
print(f"Change Owed: {n}")