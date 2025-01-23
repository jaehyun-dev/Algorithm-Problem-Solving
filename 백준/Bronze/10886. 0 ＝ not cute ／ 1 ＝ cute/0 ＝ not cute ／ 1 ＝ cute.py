N = int(input())
d = {0: 0, 1: 0}
for _ in range(N):
    d[int(input())] += 1
print("Junhee is ", end="")
if d[1] < d[0]:
    print("not ", end="")
print("cute!")