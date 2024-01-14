N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = [x - y for x, y in zip(a, b)]
r = 0
s = 0
for i in d:
    if 0 < i:
        r += i
    else:
        s += i
print(max(r, - s))