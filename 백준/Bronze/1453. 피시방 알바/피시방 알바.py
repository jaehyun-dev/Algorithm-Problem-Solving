N = int(input())
l = list(map(int, input().split()))
check = [0] * 100
cnt = 0
for i in l:
    if not check[i - 1]:
        check[i - 1] = 1
    else:
        cnt += 1
print(cnt)