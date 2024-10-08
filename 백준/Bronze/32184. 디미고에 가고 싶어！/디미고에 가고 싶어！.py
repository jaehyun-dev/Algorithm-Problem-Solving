A, B = map(int, input().split())
ans = (B - A + 2) // 2
if not A % 2 and B % 2:
    ans += 1
print(ans)