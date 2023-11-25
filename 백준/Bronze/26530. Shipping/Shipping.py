n = int(input())
for _ in range(n):
    x = int(input())
    cnt = 0
    for _ in range(x):
        a, b, c = input().split()
        cnt += int(b) * float(c)
    print("$" + format(cnt, '.2f'))