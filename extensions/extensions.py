s = input("Filename: ").lower().strip()

if s.endswith('.gif'):
    print(f"image/{s.split('.')[1]}")
elif s.endswith('.jpg'):
    print("image/jpeg")
elif s.endswith('.jpeg'):
    print(f"image/{s.split('.')[1]}")
elif s.endswith('.png'):
    print(f"image/{s.split('.')[1]}")
elif s.endswith('.pdf'):
    print(f"application/pdf")
elif s.endswith('.txt'):
    print("text/plain")
elif s.endswith('.zip'):
     print(f"application/{s.split('.')[1]}")
else:
    print("application/octet-stream")