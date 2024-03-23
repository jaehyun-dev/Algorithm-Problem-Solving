import sys
input = sys.stdin.readline
while 1:
    a = input().strip()
    if a == '*':
        break
    l = len(a)
    flag = True
    for i in range(l - 2):
        v = []
        for j in range(l - 1 - i):
            s = a[j] + a[j + i + 1]
            v.append(s)
        if len(v) != len(set(v)):
            flag = False
            break
    if flag:
        ans = ''
    else:
        ans = "NOT "
    print(f"{a} is {ans}surprising.")