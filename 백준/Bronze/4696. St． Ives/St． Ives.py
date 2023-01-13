while True:
    a = float(input())
    if a == 0:
        break
    print(format(round(1 + a + a * a + a ** 3 + a ** 4, 2), '.2f'))