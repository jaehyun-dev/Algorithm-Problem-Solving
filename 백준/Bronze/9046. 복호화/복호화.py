T = int(input())
for _ in range(T):
    l = input()
    d = {}
    for i in l:
        if i != " ":
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    M = 0
    a = []
    for i in d:
        if M < d[i]:
            M = d[i]
            a = [i]
        elif M == d[i]:
            a.append(i)
    if len(a) == 1:
        print(a[0])
    else:
        print("?")