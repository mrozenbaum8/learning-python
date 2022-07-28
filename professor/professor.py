import random
import sys

def main():
    lvl = get_level()
    score = 0

    for j in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        z = x + y

        for i in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == z:
                    score += 1
                    break
                elif i == 2:
                    print("EEE")
                    print(f"{x} + {y} = {z}")
                else:
                    print("EEE")
            except ValueError:
                if i == 2:
                    print("EEE")
                    print(f"{x} + {y} = {z}")
                else:
                    print("EEE")
                    pass
    print(f"Score: {score}")
    sys.exit(0)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                if n == 1:
                    return n
                if n == 2:
                    return n
                if n == 3:
                    return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        random_n = random.randint(0, 9)
        return random_n
    elif level == 2:
        random_n = random.randint(10, 99)
        return random_n
    else:
        random_n = random.randint(100, 999)
        return random_n


if __name__ == "__main__":
    main()