A, B = map(int, input().split())
C = int(input())
print((A + B) if A + B < 2 * C else A + B - 2 * C)