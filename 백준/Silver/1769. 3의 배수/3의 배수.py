X = input()
cnt = 0
while 1 < len(X):
    Y = 0
    for i in X:
        Y += int(i)
    cnt += 1
    X = str(Y)
print(cnt)
print("YES" if int(X) % 3 == 0 else "NO")