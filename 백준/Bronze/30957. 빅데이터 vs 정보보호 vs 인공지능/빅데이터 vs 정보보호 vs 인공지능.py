N = int(input())
s = input()
l = ["B", "S", "A"]
d = {"B": 0,
     "S": 0,
     "A": 0}
for i in s:
    flag = False
    for c in l:
        if i == c:
            d[c] += 1
            flag = True
        if flag:
            break
max_num = max(d.values())
if len(set(d.values())) == 1:
    print("SCU")
else:
    for c in l:
        if d[c] == max_num:
            print(c, end="")