while 1:
    S = input()
    if S == '0':
        break
    while 1 < len(S):
        print(S, end=" ")
        m = 1
        for i in S:
            m *= int(i)
        S = str(m)
    print(S)