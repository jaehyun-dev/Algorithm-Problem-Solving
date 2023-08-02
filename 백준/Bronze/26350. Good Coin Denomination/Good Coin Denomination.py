import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    flag = 1
    for i in range(2, l[0] + 1):
        if l[i] < 2 * l[i - 1]:
            flag = 0
            break
    print("Denominations: ", end="")
    print(*l[1:])
    print("Goo" if flag else "Ba", end="")
    print("d coin denominations!\n")