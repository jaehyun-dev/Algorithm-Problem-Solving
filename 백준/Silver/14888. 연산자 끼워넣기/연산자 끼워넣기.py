import sys, itertools
input = sys.stdin.readline
INF = int(1e9)

def oper(a, b, o):
    if o == 0:
        return a + b
    elif o == 1:
        return a - b
    elif o == 2:
        return a * b
    elif o == 3:
        if a < 0:
            return -(-a // b)
        else:
            return a // b

N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))
op = [0] * O[0] + [1] * O[1] + [2] * O[2] + [3] * O[3]
perm = set()

l = -INF
s = INF

for case in itertools.permutations(op, N - 1):
    if case in perm:
        continue
    perm.add(case)
    a = A[0]
    for i in range(N - 1):
        a = oper(a, A[i + 1], case[i])
    if a > l:
        l = a
    if a < s:
        s = a
print(l)
print(s)