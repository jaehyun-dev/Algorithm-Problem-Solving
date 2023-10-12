def find(p, x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p, p[x])
        return p[x]

def union(p, x, y):
    s = min(x, y)
    l = max(x, y)
    p[find(p, l)] = find(p, s)

def solution(n, wires):
    answer = n

    for i in range(n - 1):
        p = [0] + [*range(1, n + 1)]
        temp = wires[:i] + wires[i + 1:]
        for j in range(n - 2):
            x, y = temp[j]
            union(p, x, y)
        cnt_dic = {}
        for j in range(1, n + 1):
            if find(p, j) in cnt_dic:
                cnt_dic[find(p, j)] += 1
            else:
                cnt_dic[find(p, j)] = 1
        a = list(cnt_dic.values())
        answer = min(answer, abs(a[0] - a[1]))

    return answer

print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))