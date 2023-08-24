N = int(input())
map = []
for _ in range(N):
    map.append(input())
K = int(input())
if K == 1:
    for i in range(N):
        print(map[i])
elif K == 2:
    for i in range(N):
        print(map[i][::-1])
else:
    for i in range(N):
        print(map[N - 1 - i])