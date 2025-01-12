n = int(input())
s = 1
i = 1
j = 1
while s < n:
    j += 4 * i
    s += j
    i += 1
print(i if s == n else i - 1)