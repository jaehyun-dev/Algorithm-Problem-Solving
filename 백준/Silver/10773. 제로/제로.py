import sys
k = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(k):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)
print(sum(arr))