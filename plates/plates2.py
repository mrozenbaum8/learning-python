import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    i = 0
    num_count = 0
    for i in range(len(s)):
        if s[i].isnumeric() == True and num_count == 0:
            if s[i] == '0':
                return False
            else:
                num_count =+ 1
        elif s[i].isnumeric() == True:
            num_count += 1
    for i in range(len(s) // 2):
        if s[i].isnumeric():
            return False
    for i in s:
        if i in string.punctuation:
            return False

    else:
        return True

main()