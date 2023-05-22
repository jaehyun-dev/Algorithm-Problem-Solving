from itertools import combinations as comb
X = list(map(int, input().split()))
count = 0
for i in comb(X, 2):
    count += i[0] or i[1]
for j in comb(X, 3):
    count += j[0] or j[1] or j[2]
print(0 if count % 2 == 0 else 1)