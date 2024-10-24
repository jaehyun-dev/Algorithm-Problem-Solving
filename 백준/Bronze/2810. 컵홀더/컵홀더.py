N = int(input())
S = input()
cnt = 0
i = 0
while i < N:
    s = S[i]
    if s == "L":
        i += 1
    cnt += 1
    i += 1
print(min(N, cnt + 1))