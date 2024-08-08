d = {}
for i in range(5):
    for j in range(3):
        d[chr(i * 3 + j + 65)] = str(i + 2)
for i in range(4):
    d[chr(i + 65 + 15)] = '7'
for i in range(3):
    d[chr(i + 65 + 19)] = '8'
for i in range(4):
    d[chr(i + 65 + 22)] = '9'
d2 = {}
M = int(input())
for _ in range(M):
    a = input()
    b = ""
    for i in a:
        b += d[i]
    if b not in d2:
        d2[b] = a
N = int(input())
l = list(input().split())
w = ""
for i in l:
    if i == '1':
        if w in d2:
            print(d2[w], end=" ")
        else:
            print("*" * len(w), end=" ")
        w = ""
    else:
        w += i
if w in d2:
    print(d2[w])
else:
    print("*" * len(w))