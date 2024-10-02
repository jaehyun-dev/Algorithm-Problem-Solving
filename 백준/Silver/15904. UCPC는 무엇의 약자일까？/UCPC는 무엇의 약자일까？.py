s = input()
t = "UCPC"
i = -1
flag = 1
for c in t:
    i = s.find(c, i + 1)
    if i == -1:
        flag = 0
        break
ans = "hate"
if flag:
    ans = "love"
print(f"I {ans} UCPC")