t = float(input())
while 1:
    c = float(input())
    if c == 999:
        break
    print(format(c - t, '.2f'))
    t = c