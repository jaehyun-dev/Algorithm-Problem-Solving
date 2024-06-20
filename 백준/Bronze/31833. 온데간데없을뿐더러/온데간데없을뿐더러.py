N = int(input())
A = input().split()
B = input().split()
X, Y = "", ""
for a in A:
    X += a
for b in B:
    Y += b
print(min(int(X), int(Y)))