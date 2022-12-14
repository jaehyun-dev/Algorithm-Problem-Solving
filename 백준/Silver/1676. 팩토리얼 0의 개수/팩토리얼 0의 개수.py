n = int(input())
def base(n):
    count_2 = 0
    count_5 = 0
    while True:
        if n % 2 == 0:
            count_2 += 1
            n /= 2
        elif n % 5 == 0:
            count_5 += 1
            n /= 5
        else:
            break
    return [count_2, count_5]
ans = [0, 0]
for i in range(1, n + 1):
    ans[0] += base(i)[0]
    ans[1] += base(i)[1]

print(min(ans))