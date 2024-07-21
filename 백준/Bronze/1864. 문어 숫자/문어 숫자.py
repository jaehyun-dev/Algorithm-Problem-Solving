d = {'-': 0 , '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while 1:
    a = input()
    if a == '#':
        break
    l = len(a)
    n = 0
    for i in range(l):
        n += d[a[i]] * (8 ** (l - i - 1))
    print(n)