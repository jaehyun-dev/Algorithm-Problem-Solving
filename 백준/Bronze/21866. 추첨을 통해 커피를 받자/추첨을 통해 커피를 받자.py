s = [100, 100, 200, 200, 300, 300, 400, 400, 500]
l = list(map(int, input().split()))
flag = 0
for i in range(9):
    if s[i] < l[i]:
        flag = 1
        break
if flag:
    print("hacker")
elif 100 <= sum(l):
    print("draw")
else:
    print("none")