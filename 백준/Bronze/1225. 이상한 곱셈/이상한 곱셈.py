A, B = input().split()
a = b = 0
for i in A:
    a += int(i)
for i in B:
    b += int(i)
print(a * b)