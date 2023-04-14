N = int(input())
if N == 1:
    print(2)
else:
    print((N // 2 + 1) * (N - N // 2 + 1))