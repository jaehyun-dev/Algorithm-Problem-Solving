n = int(input())
def f(n):
    if n == 0:
        return 1
    elif n > 0:
        a = 1
        for i in range(1, n + 1):
            a = (a * i) % 10
        return a
print(f(n) if n < 5 else 0)