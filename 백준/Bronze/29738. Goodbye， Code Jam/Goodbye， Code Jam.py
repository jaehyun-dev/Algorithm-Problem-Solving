T = int(input())
for t in range(1, T + 1):
    ans = "Round "
    N = int(input())
    if 4500 < N:
        ans += "1"
    elif 1000 < N:
        ans += "2"
    elif 25 < N:
        ans += "3"
    else:
        ans = "World Finals"
    print(f"Case #{t}: {ans}")