T = int(input())
for _ in range(T):
    X = input()
    s = set()
    for i in X:
        s.add(i)
    print(len(s))