months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if date[0].isalpha():
            a, b, c = date.split(' ')
            if ',' in date:
                b = int(b.strip(','))
                month = months.index(a) + 1
                if month <= 12 and b <= 31:
                    print(f"{c}-{month:02}-{b:02}")
                    break
                else:
                    pass
            else:
                pass
        else:
            d, e, f = date.split('/')
            d = int(d)
            e = int(e)
            f = int(f)
            if d <= 12 and e <= 31:
                print(f"{f}-{d:02}-{e:02}")
                break
            else:
                pass
    except ValueError:
        pass