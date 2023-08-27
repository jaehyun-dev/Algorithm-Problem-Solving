import itertools
a = list()
for _ in range(9):
    a.append(int(input()))
for i in itertools.combinations(a, 7):
    if sum(i) == 100:
        for j in range(7):
            print(sorted(i)[j])
        break