e, f, c = map(int, input().split())
e += f
ans = 0
while c <= e:
    n = e // c
    ans += n
    e = e % c + n
print(ans)