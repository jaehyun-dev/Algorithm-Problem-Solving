N, X = map(int, input().split())
T = list(map(int, input().split()))
i = 0
while 1:
    if T[i] < X:
        break
    i = (i + 1) % N
    X += 1
print(i + 1)