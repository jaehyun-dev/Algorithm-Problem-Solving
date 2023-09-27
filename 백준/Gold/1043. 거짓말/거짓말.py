def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    m = min(x, y)
    M = max(x, y)
    p_x = find(m)
    p_y = find(M)
    if p_x != p_y:
        p[p_y] = p_x

N, M = map(int, input().split())
p = [*range(N + 1)]
a = list(map(int, input().split()))
T = a[0]
t_list = sorted(a[1:])
M_list = []
for _ in range(M):
    b = list(map(int, input().split()))
    P = b[0]
    p_list = b[1:]
    M_list.append(p_list)
    t_ = min(p_list)
    for i in range(P):
        if p_list[i] in t_list:
            t_ = p_list[i]
            break
    for i in range(P):
        union(t_, p_list[i])
cnt = 0
for m in M_list:
    flag = True
    for i in m:
        if find(i) in list(map(lambda x: find(x), t_list)):
            flag = False
            pass
    if flag:
        cnt += 1
print(cnt)