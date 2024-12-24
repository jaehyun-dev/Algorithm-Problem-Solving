while 1:
    l = input().split()
    if l == ["#"]:
        break
    C = T = 0
    for i in l[:-1]:
        if i == 'A':
            C += 1
        else:
            if int(i) % 2:
                C += 1
            else:
                T +=1
    if C < T:
        print("Tania")
    elif T < C:
        print("Cheryl")
    else:
        print("Draw")