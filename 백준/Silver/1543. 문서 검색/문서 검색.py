d = input()
w = input()
l = len(w)
cnt = 0
i = 0
while i <= len(d) - l:
    n = d.find(w, i)
    if n == -1:
        break
    i = n + l
    cnt += 1
print(cnt)