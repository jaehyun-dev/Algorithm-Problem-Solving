N = int(input())
M = int(input())
t = "IO" * N + "I"
S = input()
i = 0
cnt = 0
while i < len(S):
    idx = S.find(t, i)
    if idx == -1:
        break
    i = idx + 1
    cnt += 1
print(cnt)