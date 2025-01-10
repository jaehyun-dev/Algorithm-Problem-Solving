ji = "ABCDEFGHIJKL"
N = int(input())
gapja = (N - 4) % 60
ans = ji[gapja % 12] + str(gapja % 10)
print(ans)