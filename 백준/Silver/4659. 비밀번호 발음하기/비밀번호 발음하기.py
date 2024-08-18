v = ('a', 'e', 'i', 'o', 'u')
while 1:
    p = input()
    if p == "end":
        break
    flag = 0
    s = set(p)
    for i in p:
        if i in v:
            flag = 1
            break
    if flag:
        cv = 0
        cc = 0
        if p[0] in v:
            cv = 1
            prev = "vo"
        else:
            cc = 1
            prev = "co"
        for i in range(1, len(p)):
            if prev == "vo":
                if p[i] in v:
                    cv += 1
                    if cv == 3:
                        flag = 0
                        break
                else:
                    cv = 0
                    cc = 1
                    prev = "co"
            else:
                if p[i] not in v:
                    cc += 1
                    if cc == 3:
                        flag = 0
                        break
                else:
                    cv = 1
                    cc = 0
                    prev = "vo"
        if flag:
            for i in s:
                if i not in ('e', 'o') and i * 2 in p:
                    flag = 0
    b = "" if flag else "not "
    print(f"<{p}> is {b}acceptable.")