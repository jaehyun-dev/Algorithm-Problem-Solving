def fibonacci(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 2] + arr[i - 1])
    return arr[n]

n = int(input())
for _ in range(n):
    a = int(input())
    print(fibonacci(a - 1), fibonacci(a))