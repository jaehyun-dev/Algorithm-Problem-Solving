A, B = map(int, input().split())
cnt = 1
i = 0
j = 2
while i < B:
    cnt += j * (A - 2) - (A -3)
    i += 1
    j += 1
print(cnt)