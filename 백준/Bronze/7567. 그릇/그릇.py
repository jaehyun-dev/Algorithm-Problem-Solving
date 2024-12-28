b = input()
h = 10
p = b[0]
for i in b[1:]:
    c = i
    if p == c:
        h += 5
    else:
        h += 10
    p = c
print(h)