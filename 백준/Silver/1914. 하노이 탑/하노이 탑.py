def hanoi(start, end, n):
    temp = list(set.difference(set(l), {start, end}))[0]
    if n == 0:
        return
    elif n == 1:
        print(start, end)
    else:
        hanoi(start, temp, n - 1)
        print(start, end)
        hanoi(temp, end, n - 1)

l = [1, 2, 3]
N = int(input())
print(2 ** N - 1)
if N <= 20:
    hanoi(1, 3, N)