import sys
input = sys.stdin.readline
while 1:
    ans = 0
    a = input().strip()
    if a == '0':
        break
    for i in list(a):
        if i == '1':
            ans += 2
        elif i == '0':
            ans += 4
        else:
            ans += 3
    ans += len(list(a)) + 1
    print(ans)