N = int(input())
a = [input()]
for _ in range(N - 1):
    w = input()
    flag = True
    for i in range(len(a)):
        c = a[i]
        try:
            if c.index(w) == 0:
                flag = False
                break
        except:
            try:
                if w.index(c) == 0:
                    a.remove(c)
                    a.append(w)
                    flag = False
                    break
            except:
                pass
    if flag:
        a.append(w)
print(len(a))