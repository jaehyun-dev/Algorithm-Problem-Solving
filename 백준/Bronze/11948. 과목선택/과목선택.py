a = []
for _ in range(4):
    a.append(int(input()))
b = []
for _ in range(2):
    b.append(int(input()))
a.remove(min(a))
b.remove(min(b))
print(sum(a) + sum(b))