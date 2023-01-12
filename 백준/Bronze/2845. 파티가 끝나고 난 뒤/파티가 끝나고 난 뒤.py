L, P = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    print(i - (L * P), end=" ")