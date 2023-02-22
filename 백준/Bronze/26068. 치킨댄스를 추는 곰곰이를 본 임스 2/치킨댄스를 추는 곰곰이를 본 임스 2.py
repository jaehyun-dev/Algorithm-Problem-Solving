N = int(input())
count = 0
for _ in range(N):
    res = ''
    for i in list(input())[2:]:
        res += i
    if int(res) < 91:
        count += 1
print(count)