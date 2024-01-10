T = int(input())
for _ in range(T):
    N = int(input())
    print("Good" if ((N + 1) % (N % 100) == 0) else "Bye")