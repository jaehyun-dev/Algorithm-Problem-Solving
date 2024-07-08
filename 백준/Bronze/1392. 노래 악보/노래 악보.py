N, Q = map(int, input().split())
t = [int(input())]
for i in range(N - 1):
    s = int(input())
    t.append(t[i] + s)
for _ in range(Q):
    q = int(input())
    flag = 1
    for n in range(N):
        if q < t[n]:
            print(n + 1)
            flag = 0
            break
    if flag:
        print(N)