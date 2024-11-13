N = int(input())
n = []
for i in range(1, N + 1):
    n.append(str(i))
s = ''.join(n)
print(s.find(str(N)) + 1)