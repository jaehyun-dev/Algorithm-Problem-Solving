n = int(input())
S = input()
ans = ""
for i in S:
    if i == "I":
        ans += "i"
    elif i == "l":
        ans += "L"
print(ans)