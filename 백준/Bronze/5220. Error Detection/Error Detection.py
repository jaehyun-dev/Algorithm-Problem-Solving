n = int(input())
for _ in range(n):
    b, c = map(int, input().split())
    cnt = 0
    print("Valid" if bin(b)[2:].count('1') % 2 == c else "Corrupt")