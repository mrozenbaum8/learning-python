import random
import sys

while True:
    try:
        n = int(input("Level: "))
        r = random.randint(1, n)
        while True:
            try:
                g = int(input("Guess: "))
                if g == r:
                    print('Just right!')
                    sys.exit()
                elif g > r:
                    print('Too large!')
                    pass
                elif g < r:
                    print('Too small!')
                    pass
            except (ValueError, TypeError):
                pass
    except (ValueError, TypeError):
        pass