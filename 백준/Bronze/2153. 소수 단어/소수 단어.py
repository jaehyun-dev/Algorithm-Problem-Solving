a = [0] * 27
b = [0] * 26
for i in range(1, 27):
    a[i] = chr(i + 96)
for i in range(26):
    b[i] = chr(i + 65)
c = a + b
w = input()
cnt = 0
for i in w:
    cnt += c.index(i)
p = [1] * (cnt + 1)
for i in range(2, cnt // 2 + 1):
    j = 2
    n = i * j
    while n <= cnt:
        p[n] = 0
        j += 1
        n = i * j
print("It is ", end="")
if not p[cnt]:
    print("not ", end="")
print("a prime word.")