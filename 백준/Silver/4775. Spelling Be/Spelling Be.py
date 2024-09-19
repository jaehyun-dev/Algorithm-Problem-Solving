N = int(input())
d = set()
for _ in range(N):
    d.add(input())
M = int(input())
for i in range(M):
    m = []
    while 1:
        w = input()
        if w == "-1":
            break
        if w not in d:
            m.append(w)
    if m:
        print(f"Email {i + 1} is not spelled correctly.")
        for j in m:
            print(j)
    else:
        print(f"Email {i + 1} is spelled correctly.")
print("End of Output")