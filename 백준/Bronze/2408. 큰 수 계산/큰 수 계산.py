N = int(input())
c = ""
for _ in range(2 * N - 1):
    a = input()
    if a == '/':
        c += '//'
    else:
        c += a
c = f'print({c})'
exec(c)