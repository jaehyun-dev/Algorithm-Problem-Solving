flag = 1
d = set()
for _ in range(3):
    c = input()[0]
    if c not in ['l', 'k', 'p'] or c in d:
        flag = 0
        break
    d.add(c)
print("GLOBAL" if flag else "PONIX")