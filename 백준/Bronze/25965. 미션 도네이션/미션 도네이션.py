N = int(input())
for n in range(N):
    ans = 0
    M = int(input())
    mission = []
    for _ in range(M):
        mission.append(tuple(map(int, input().split())))
    d = tuple(map(int, input().split()))
    for m in mission:
        cnt = 0
        cnt += d[0] * m[0] - d[1] * m[1] + d[2] * m[2]
        if 0 < cnt:
            ans += cnt
    print(ans)