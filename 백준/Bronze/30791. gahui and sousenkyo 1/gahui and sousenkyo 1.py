V = list(map(int, input().split()))
cnt = 0
for i in range(1, 5):
    if V[0] - V[i] <= 1000:
        cnt += 1
print(cnt)