def solution(common):
    a, b, c = common[-3:][::-1]
    if a - b == b - c:
        answer = a + (a - b)
    else:
        answer = a * (a / b)
    return answer