N = int(input())
cnt = s = start = end = 0
while end <= N:
    if s < N:
        end += 1
        s += end
    elif N < s:
        s -= start
        start += 1
    else:
        cnt += 1
        end += 1
        s += end
print(cnt)