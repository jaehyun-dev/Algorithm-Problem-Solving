N = int(input())
a = []
p = "Present!"
prev = p
for _ in range(N):
    c = input()
    if prev != p and c != p:
        a.append(prev)
    prev = c
if prev != p:
    a.append(prev)
if len(a) == 0:
    print("No Absences")
else:
    for i in a:
        print(i)