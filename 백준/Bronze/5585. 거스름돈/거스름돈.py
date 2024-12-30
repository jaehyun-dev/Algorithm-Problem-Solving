c = [500, 100, 50, 10, 5, 1]
p = int(input())
r = 1000 - p
cnt = 0
for i in c:
    cnt += r // i
    r %= i
print(cnt)