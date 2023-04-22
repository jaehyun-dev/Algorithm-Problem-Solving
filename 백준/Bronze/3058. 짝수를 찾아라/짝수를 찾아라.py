T = int(input())
for _ in range(T):
    sum = 0
    num = 100
    for i in list(map(int, input().split())):
        if i % 2 == 0:
            sum += i
            if i < num:
                num = i
    print(sum, num)