N = int(input())
for _ in range(N):
    a, b, c, d = map(int, input().split())
    print(a, b + c + d, "PASS" if b >= 35 * .3 and c >= 25 * .3 and d >= 40 * .3 and b + c + d >= 55 else "FAIL")