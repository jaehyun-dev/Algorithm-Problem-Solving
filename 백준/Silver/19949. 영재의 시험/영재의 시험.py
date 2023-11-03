import itertools
ans = list(map(int, input().split()))
cnt = 0
for case in itertools.product(*[list(range(1, 6)) for _ in range(10)]):
    flag = False
    for i in range(2, 10):
        if case[i - 2] == case[i - 1] == case[i]:
            flag = True
            break
    if flag:
        continue
    score = 0
    for i in range(10):
        if case[i] == ans[i]:
            score += 1
    if 5 <= score:
        cnt += 1
print(cnt)