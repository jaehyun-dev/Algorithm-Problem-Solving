a = list(map(int, input().split()))
print(max(0, a[-1] * 4 - sum(a[:4])))