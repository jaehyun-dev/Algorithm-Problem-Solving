def solution(a, b, n):
    answer = 0
    new = 0
    while a <= n:
        new = (n // a) * b
        answer += new
        n = n - ((n // a) * a) + new

    return answer