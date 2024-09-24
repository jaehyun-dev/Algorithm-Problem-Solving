n = int(input())
a = 0
b = 1
i = 1
while i < n:
    a, b = b, a + b
    i += 1
print(b if n else 0)