T = int(input())
N = int(input())
F = list(map(int, input().split()))
print("Padaeng_i", end=" ")
print("Happy" if T <= sum(F) else "Cry")