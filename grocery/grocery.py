groceries = {}

while True:
    try:
        item = input("")
        if item in groceries:
            groceries[item] += 1
        elif item not in groceries:
            groceries[item] = 1

    except ValueError:
        pass

    except EOFError:
        for food in sorted(groceries):
            print(f"{groceries[food]} {food.upper()}")
        break