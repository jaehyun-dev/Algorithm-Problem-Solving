while 1:
    g = int(input())
    if not g:
        break
    num = [0] + [1] * 10
    l, h = 1, 11
    while 1:
        a = input()
        if a == "too high":
            for i in range(g, h):
                num[i] = 0
            h = g
        elif a == "too low":
            for i in range(l, g + 1):
                num[i] = 0
            l = g + 1
        else:
            if sum(num) and num[g]:
                print("Stan may be honest")
            else:
                print("Stan is dishonest")
            break
        g = int(input())