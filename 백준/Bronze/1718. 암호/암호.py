p = input()
k = input()
ans = ""
i = 0
j = 0
while i < len(p):
    if p[i] == " ":
        ans += " "
    else:
        d = ord(p[i]) - ord(k[j])
        d = (d - 1) % 26 + 1
        ans += chr(96 + d)
    i += 1
    j += 1
    if j == len(k):
        j = 0
print(ans)