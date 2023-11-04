N, U, L = map(int, input().split())
if 999 < N:
    if 7999 < U or 259 < L:
        print("Very Good")
    else:
        print("Good")
else:
    print("Bad")