from cs50 import get_float

while True:
    cents = get_float("Change owed: ")
    if 0 < cents:
        break

quarters = int(cents / .25)
cents = cents - quarters * .25

dimes = round(cents / .10)
cents = cents - dimes * .10

nickels = round(cents / .05)
cents = cents - nickels * .05

pennies = round(cents / .01)
cents = cents - pennies * .01

coins = quarters + dimes + nickels + pennies

print(f"{coins}")