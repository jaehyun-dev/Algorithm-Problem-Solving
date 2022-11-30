a = int(input())
b = int(input())
c = int(input())
n = [int(x) for x in str(a * b * c)]
dic = {x: n.count(x) for x in n}
for i in range(10):
    if i not in dic:
        dic[i] = 0
for i in range(10):
    print(dic[i])