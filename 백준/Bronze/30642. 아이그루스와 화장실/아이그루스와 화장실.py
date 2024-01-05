N = int(input())
m = input()[0]
K = int(input())
f = 1
if m == 'i':
    f = 0
ans = K + (K + f) % 2
if N < ans:
    ans -= 2
print(ans)