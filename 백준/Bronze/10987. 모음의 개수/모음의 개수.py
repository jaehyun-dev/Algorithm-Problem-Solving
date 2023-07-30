a = set(["a", "e", "i", "o", "u"])
b = 0
c = input()
for i in c:
    if i in a:
        b += 1
print(b)