S = int(input())
s = 0
i = 1
while 1:
    s += i
    if S < s:
        break
    i += 1
print(i - 1)