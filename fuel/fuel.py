while True:
    try:
        a, b = input("Fraction: ").split("/")
        a = int(a)
        b = int(b)
        c = (a / b) * 100

        if a <= b:
            if c == 0 or c == 1:
                print("E")
                break
            if c == 99 or c == 100:
                print("F")
                break
            print(f"{round(c)}%")
            break
        else:
            pass

    except ValueError:
        pass
    except ZeroDivisionError:
        pass