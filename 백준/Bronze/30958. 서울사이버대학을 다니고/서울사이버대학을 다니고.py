N = int(input())
a = input()
d = {}
for n in range(N):
    if a[n] == " " or a[n] == "," or a[n] == ".":
        continue
    if a[n] in d:
        d[a[n]] += 1
    else:
        d[a[n]] = 1
print(max(d.values()))