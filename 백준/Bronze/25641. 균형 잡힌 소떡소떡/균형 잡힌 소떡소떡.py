N = int(input())
a = input()
sc = a.count("s")
tc = a.count("t")
i = 0
while sc != tc:
    c = a[i]
    if c == "s":
        sc -= 1
    else:
        tc -= 1
    i += 1
print(a[i:])