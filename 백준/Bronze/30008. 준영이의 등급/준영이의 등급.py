def grade(x):
    p = [4, 11, 23, 40, 60, 77, 89, 96, 100]
    for i in range(11):
        if x <= p[i]:
            return i + 1
    return 9

N, K = map(int, input().split())
G = list(map(int, input().split()))
P = list(map(lambda x: x * 100 // N, G))
S = list(map(grade, P))
print(*S)