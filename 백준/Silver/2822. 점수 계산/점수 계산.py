M = [0] * 5
idx = [0] * 5
for i in range(8):
    n = int(input())
    for j in range(5):
        if M[j] < n:
            M = M[:j] + [n] + M[j:4]
            idx = idx[:j] + [i] + idx[j:4]
            break
print(sum(M))
print(*map(lambda x: x + 1, sorted(idx)))