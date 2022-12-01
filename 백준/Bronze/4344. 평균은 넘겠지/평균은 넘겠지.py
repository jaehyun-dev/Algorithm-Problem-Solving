c = int(input())
for _ in range(c):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    count = 0
    for i in range(n):
        avr = sum(arr) / len(arr)
        if arr[i] > avr:
            count += 1
    print(f"{format((round((count / len(arr) * 100), 3)), '.3f')}%")