N = int(input())
F = int(input())
n = N // 100 * 100
for i in range(n, n + 100):
    if not i % F:
        print(str(i)[-2:])
        break