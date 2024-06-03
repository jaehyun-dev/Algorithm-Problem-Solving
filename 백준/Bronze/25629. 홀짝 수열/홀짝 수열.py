N = int(input())
a = list(map(int, input().split()))
o = 0
for i in a:
    if i % 2:
        o += 1
print(int(o == (N + 1) // 2))