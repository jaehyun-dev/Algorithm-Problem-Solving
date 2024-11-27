def a(s):
    global p
    if p == 1:
        if s == 'A':
            p = 2
        elif s == 'C':
            p = 3
    elif p == 2:
        if s == 'A':
            p = 1
        elif s == 'B':
            p = 3
    else:
        if s == 'B':
            p = 2
        elif s == 'C':
            p = 1
o = input()
p = 1
for s in o:
    a(s)
print(p)