from itertools import combinations as cmb
l = [0] * 9
for i in range(9):
    l[i] = int(input())
for i in cmb(l, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break