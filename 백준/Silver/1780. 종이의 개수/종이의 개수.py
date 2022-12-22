import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
count_n1, count_0, count_1 = 0, 0, 0

def recursion(n, x, y):
    global count_n1, count_0, count_1
    check = graph[x][y]
    flag = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != check:
                flag = True
                break
    if flag:
        n //= 3
        for i in range(3):
            for j in range(3):
                recursion(n, x + (i * n), y + (j * n))
    elif check == -1:
        count_n1 += 1
    elif check == 0:
        count_0 += 1
    elif check == 1:
        count_1 += 1

recursion(n, 0, 0)
print(count_n1, count_0, count_1, sep='\n')