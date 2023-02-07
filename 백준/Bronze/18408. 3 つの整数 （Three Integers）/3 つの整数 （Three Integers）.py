import collections
A = list(map(int, input().split()))
counter = collections.Counter(A)
print(counter.most_common()[0][0])