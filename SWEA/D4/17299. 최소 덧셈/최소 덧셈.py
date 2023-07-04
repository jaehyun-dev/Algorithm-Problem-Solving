T = int(input())
for i in range(1, T + 1):
    a = input()
    m = int(a)
    for j in range(1, len(a)):
        n1 = a[:j]
        n2 = a[j:]
        if n2[0] != '0':
            m = min(m, int(n1) + int(n2))
    print(f"#{i} {m}")