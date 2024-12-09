while 1:
    b = input()
    if b == "#":
        break
    c = 0
    flag = 0
    for i in b:
        if i == '1':
            c += 1
        if i == 'e':
            flag = 1
    b = b[:-1]
    if flag:
        if c % 2:
            b += '1'
        else:
            b += '0'
    else:
        if c % 2:
            b += '0'
        else:
            b += '1'
    print(b)