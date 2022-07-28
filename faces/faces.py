def convert(string_s):
    i = string_s.replace(":)", "🙂").replace(":(", "🙁")
    return i

def main():
    s = input("")
    print(convert(s))

main()