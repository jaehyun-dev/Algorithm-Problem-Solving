A = list(input())
B = input().split()
for b in B:
    for i in range(len(A)):
        if A[i] == b:
            A[i] = chr(ord(A[i]) + 32)
print("".join(A))