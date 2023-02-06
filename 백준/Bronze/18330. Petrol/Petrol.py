n, k = int(input()), int(input())
print(n * 1500 if n <= k + 60 else (k + 60) * 1500 + (n - (k + 60)) * 3000)