W = [0] * 3
K = [0] * 3
for _ in range(10):
    s = int(input())
    if W[0] < s:
        W[0] = s
    W.sort()
for _ in range(10):
    s = int(input())
    if K[0] < s:
        K[0] = s
    K.sort()
print(sum(W), sum(K))