K = int(input())
a1 = 'G' * K + '.' * K * 3
a2 = '.' * K + 'I' * K + '.' * K + 'T' * K
a3 = '.' * K * 2 + 'S' * K + '.' * K
a = [a1, a2, a3]
for i in a:
    for _ in range(K):
        print(i)