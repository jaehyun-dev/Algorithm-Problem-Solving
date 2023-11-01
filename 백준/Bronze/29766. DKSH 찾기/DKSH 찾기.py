s = input()
cnt = 0
i = 0
while i < len(s) - 4:
    idx = s.find("DKSH", i)
    if idx != -1:
        i = s.index("DKSH", i) + 1
        cnt += 1
    else:
        break
print(cnt)