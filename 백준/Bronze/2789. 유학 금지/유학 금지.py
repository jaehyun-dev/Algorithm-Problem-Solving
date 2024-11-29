s = set()
for i in "CAMBRIDGE":
    s.add(i)
w = input()
ans = ""
for i in w:
    if i not in s:
        ans += i
print(ans)