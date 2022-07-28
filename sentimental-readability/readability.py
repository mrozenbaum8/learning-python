from cs50 import get_string

text = get_string("Text: ")
letters = len(text)
letters = letters - text.count(' ') - text.count('.') - text.count('!') - text.count('?') - text.count(',') - text.count('"') - text.count("'")
words = text.count(' ') + 1
sentences = text.count('.') + text.count('!') + text.count('?')

L = ((letters / words) * 100)
S = ((sentences / words) * 100)
index = ((0.0588 * L) - (0.296 * S) - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 1 and index <= 16:
    print(f"Grade {round(index)}")
else:
    print("Grade 16+")