import sys
n = int(input())
stack = []
ans = []
num = 0
flag = True

for i in range(n):
    a = int(sys.stdin.readline().strip())

    while num < a:
        num += 1
        stack.append(num)
        ans.append("+")

    if stack[-1] == a:
        stack.pop()
        ans.append("-")
    else:
        flag = False
        break

if flag == True:
    for i in ans:
        print(i)
else:
    print("NO")