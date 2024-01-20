P = int(input())
c = {1: 0,
     2: 0,
     3: 1,
     4: 2
}
s = [0] * 4
for _ in range(P):
    G, C, N = map(int, input().split())
    if G == 1:
        s[3] += 1
    else:
        s[c[C]] += 1
for i in s:
    print(i)