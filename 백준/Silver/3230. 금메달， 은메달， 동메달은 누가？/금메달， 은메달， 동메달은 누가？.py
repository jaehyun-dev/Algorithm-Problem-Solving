N, M = map(int, input().split())
first = []
for i in range(N):
    first.insert(int(input()) - 1, i + 1)
second = []
for n in first[:M][::-1]:
    second.insert(int(input()) - 1, n)
for i in range(3):
    print(second[i])