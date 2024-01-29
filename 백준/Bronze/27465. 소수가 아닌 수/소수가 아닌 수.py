N = int(input())
if N == 1 or N == 2:
    print(4)
elif N == int(1e9):
    print(int(1e9))
elif N % 2 == 0:
    print(N)
else:
    print(N + 1)