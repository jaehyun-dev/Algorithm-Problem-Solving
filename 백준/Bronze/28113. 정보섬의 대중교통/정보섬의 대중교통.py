N, A, B = map(int, input().split())
if N <= A == B:
    print("Anything")
elif N <= B < A:
    print("Subway")
else:
    print("Bus")