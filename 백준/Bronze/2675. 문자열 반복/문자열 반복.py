n = int(input())
for _ in range(n):
    arr = input().split()
    R, S = int(arr[0]), arr[1]
    for i in S:
        print(i * R, end="")
    print()