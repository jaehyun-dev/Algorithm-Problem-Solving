n = int(input())
S = input()
cnt = n
for i in ["u", "o", "s", "p", "c"]:
    c = S.count(i)
    if c < cnt:
        cnt = c
print(cnt)