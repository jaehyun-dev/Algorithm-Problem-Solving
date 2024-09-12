def move(disk, start, end):
    print(start, end)

def hanoi(n, start, end):
    temp = 6 - start - end
    if n < 1:
        return
    elif n == 1:
        move(n, start, end)
    else:
        hanoi(n - 1, start, temp)
        move(n, start, end)
        hanoi(n - 1, temp, end)

N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)