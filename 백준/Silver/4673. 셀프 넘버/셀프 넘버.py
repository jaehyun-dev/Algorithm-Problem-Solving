def d(n):
    arr = list(map(int, str(n)))
    count = n
    for i in range(len(arr)):
        count += arr[i]
    return count

N = 10000
arr = [True] * N

i = 1
while i <= N:
    if d(i) <= N and arr[d(i) - 1] == True:
        arr[d(i) - 1] = False
    i += 1

for i in range(N):
    if arr[i] == True:
        print(i + 1)