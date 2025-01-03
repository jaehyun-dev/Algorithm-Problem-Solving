while 1:
    c = input()
    if c == "*":
        break
    flag = 1
    for i in range(97, 123):
        if chr(i) not in c:
            flag = 0
            break
    print("Y" if flag else "N")