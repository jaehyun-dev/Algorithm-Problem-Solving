N = int(input())
l = []
c = {}
for i in range(N):
    c[i + 1] = 0
for _ in range(N):
    a = tuple(map(int, input().split()))
    l.append(a)
l.sort(key= lambda x:(x[2],x[0]), reverse=True)
i = 0
count = 0
while True:
    if c[l[i][0]] < 2:
        c[l[i][0]] += 1
        print(l[i][0], l[i][1])
        count += 1
    if count == 3:
        break
    i += 1