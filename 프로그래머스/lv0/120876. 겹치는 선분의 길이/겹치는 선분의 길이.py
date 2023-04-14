import itertools
def solution(lines):
    points = [set(range(l[0], l[1])) for l in lines]
    ans = set([])
    for i in itertools.combinations(points, 2):
        ans |= i[0] & i[1]
    return len(ans)