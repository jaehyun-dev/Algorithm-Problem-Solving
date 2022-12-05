import sys
n = int(input())
for _ in range(n):
    string = sys.stdin.readline().strip()
    count = 0
    for i in range(len(string)):
        if string[i] == '(':
            count += 1
        elif string[i] == ')':
            count -= 1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")