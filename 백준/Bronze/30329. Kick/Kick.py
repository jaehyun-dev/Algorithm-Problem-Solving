s = input()
cnt = 0
i = 0
while i < len(s) - 4:
    try:
        i = s.index("kick", i)
        cnt += 1
        i += 3
    except:
        break
print(cnt)