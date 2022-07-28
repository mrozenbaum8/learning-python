import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
    text = input("Input (w/ random font): ")
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and sys.argv[1] == '-f' or sys.argv[1] == '-font':
    if sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
        text = input("Input (w/ custom font): ")
        print(figlet.renderText(text))
    else:
        print("Font unavailable")
else:
   sys.exit("Usage: python figlet.py or python figlet.py -f ")