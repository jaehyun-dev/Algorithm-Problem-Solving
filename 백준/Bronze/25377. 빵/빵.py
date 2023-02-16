N = int(input())
min_time = 1001
for _ in range(N):
    A, B = map(int, input().split())
    if A <= B:
        min_time = min(min_time, B)
print(min_time if min_time < 1001 else -1)