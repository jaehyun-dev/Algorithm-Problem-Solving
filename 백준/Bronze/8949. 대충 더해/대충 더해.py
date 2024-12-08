A, B = input().split()
l = max(len(A), len(B))
A = A.zfill(l)
B = B.zfill(l)
for i in range(l):
    print(int(A[i]) + int(B[i]), end="")