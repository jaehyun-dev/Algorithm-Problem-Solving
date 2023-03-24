from itertools import permutations as p

def check(arr):
    visited = [arr[0]]
    larger = []
    smaller = []
    i = 1
    while i < len(arr):
        for j in visited:
            if j > arr[i]:
                larger.append(j)
            if j < arr[i]:
                smaller.append(j)
            for k in larger:
                for l in smaller:
                    if visited.index(k) < visited.index(l):
                        return False
        visited.append(arr[i])
        larger = []
        smaller = []
        i += 1
    return True

n = int(input())
arr = [*range(1, n + 1)]
for i in p(arr, n):
    if check(i):
        print(*i)