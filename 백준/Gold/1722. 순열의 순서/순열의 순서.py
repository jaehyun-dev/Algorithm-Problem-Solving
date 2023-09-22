import math

def p1(N, k):
    cnt_list = [0] * N
    base_list = list(range(1, N + 1))
    ans = [0] * N
    n = N
    i = 0
    k -= 1
    while k > 0:
        c = math.factorial(n - 1)
        cnt_list[i] = k // c
        k %= c
        i += 1
        n -= 1
    for i in range(N):
        ans[i] = base_list[cnt_list[i]]
        base_list.remove(ans[i])
    return ans

def p2(N, perm):
    ans = 0
    n = N
    base_list = list(range(1, N + 1))
    for i in range(N):
        ans += base_list.index(perm[i]) * math.factorial(n - 1)
        n -= 1
        base_list.remove(perm[i])
    return ans + 1

N = int(input())
a = list(map(int, input().split()))
if a[0] == 1:
    k = a[1]
    print(*p1(N, k))
else:
    b = a[1:]
    print(p2(N, b))