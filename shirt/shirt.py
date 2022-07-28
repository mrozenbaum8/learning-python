import sys
from PIL import Image, ImageFilter
from PIL import ImageOps
import os
import PIL as pillow


file1_name, file1_ext = os.path.splitext(sys.argv[1])
file2_name, file2_ext = os.path.splitext(sys.argv[2])

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].lower().endswith('.jpg') == False and sys.argv[1].lower().endswith('.jpeg') == False and (sys.argv[1]).lower().endswith('.png') == False:
    sys.exit("Invalid input")

elif sys.argv[2].lower().endswith('.jpg') == False and sys.argv[2].lower().endswith('.jpeg') == False and (sys.argv[2]).lower().endswith('.png') == False:
    sys.exit("Invalid input")

elif file2_ext.lower() != file1_ext.lower():
    sys.exit("Invalid input")

try:
    person = Image.open(sys.argv[1], mode='r', formats=None)
    shirt = Image.open('shirt.png')
    shirt_size = shirt.size
    person = ImageOps.fit(person, shirt_size)
    person.paste(shirt, shirt)
    person.save(sys.argv[2])
    sys.exit(0)

except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)

