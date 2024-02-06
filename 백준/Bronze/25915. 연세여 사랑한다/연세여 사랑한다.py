c = ord(input())
s = "ILOVEYONSEI"
cnt = 0
for i in s:
    cnt += abs(c - ord(i))
    c = ord(i)
print(cnt)