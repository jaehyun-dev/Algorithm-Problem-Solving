Y = int(input())
while 1:
    Y += 1
    y = str(Y)
    d = set()
    flag = 1
    for i in y:
        if i in d:
            flag = 0
            break
        else:
            d.add(i)
    if flag:
        print(y)
        break