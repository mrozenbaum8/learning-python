def main():
    t = input("What time is it? ")
    dt = convert(t)

    if dt >= 7 and dt <= 8:
        print("breakfast time")

    elif dt >= 12 and dt <= 13:
        print("lunch time")

    elif dt >= 18 and dt <= 19:
        print("dinner time")

    else:
        return

def convert(time):
    hours, minutes = time.split(":")
    dec_mins = float(minutes) / float(60)
    final = float(hours) + dec_mins
    return final

if __name__ == "__main__":
    main()