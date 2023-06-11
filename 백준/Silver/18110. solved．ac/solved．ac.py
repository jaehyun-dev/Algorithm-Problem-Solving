import sys
input = sys.stdin.readline

def traditional_round(num):
    return round(num + 10 ** (-len(str(num)) - 1))

n = int(input())
flag = 1
if n == 0:
    print(0)
    flag = 0
if flag:
    l = []
    for _ in range(n):
        l.append(int(input()))
    l.sort()
    num = int(traditional_round(n * .15))
    if num == 0:
        print(int(traditional_round(sum(l) / n)))
    else:
        print(int(traditional_round(sum(l[num:-num]) / (n - 2 * num))))