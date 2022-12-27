n, k = map(int, input().split())
arr = [*range(1, n + 1)]
ans = []
count = k
num = n
while len(ans) < n:
    ans.append(arr.pop(count - 1))
    count += (k - 1)
    num -= 1
    if len(ans) == n:
        break
    while count > num:
        count -= num
        
print("<", end="")
for i in range(n - 1):
    print(f"{ans[i]}, ", end="")
print(f"{ans[-1]}>")