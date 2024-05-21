A, B, C = map(int, input().split())
N = int(input())
ans = 0
for _ in range(N):
    score = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        score += sum(x * y for x, y in zip((A, B, C), (a, b, c)))
    if ans < score:
        ans = score
print(ans)