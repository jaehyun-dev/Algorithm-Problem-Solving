T = int(input())
for _ in range(T):
    l = sorted(list(map(int, input().split())))[1:4]
    print("KIN" if 3 < l[2] - l[0] else sum(l))