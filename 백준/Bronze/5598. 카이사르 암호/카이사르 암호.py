c = input()
p = ""
for i in c:
    o = ord(i) - 3
    if o < 65:
        o += 26
    p += chr(o)
print(p)