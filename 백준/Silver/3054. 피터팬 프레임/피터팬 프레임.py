w = input()
l = len(w)
a = '.'
b = '.'
c = '#'
for i in range(l):
    if (i % 3 - 2) :
        s = '#'
    elif l % 3 != 2:
        s = '*'
    t = '.' + s +'..'
    a += t
    t = s + '.' + s + '.'
    b += t
    if i < l - 1 and i % 3 == 1:
        s = '*'
    t = '.' + w[i] + '.' + s
    c += t
print(a)
print(b)
print(c)
print(b)
print(a)