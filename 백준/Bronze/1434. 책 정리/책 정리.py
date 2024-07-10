N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
i = 0
j = 0
while j < M:
    if A[i] < B[j]:
        cnt += A[i]
        A = A[:i] + A[i + 1:]
    else:
        A[i] -= B[j]
        j += 1
        i = 0
while i < len(A):
    cnt += A[i]
    i += 1
print(cnt)