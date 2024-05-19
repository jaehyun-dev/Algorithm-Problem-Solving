import math
K = int(input())
S = input()
ans = ""
for i in range(math.ceil(len(S) / K)):
    ans += S[i * K]
print(ans)