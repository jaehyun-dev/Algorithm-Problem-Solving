def solution(n):
    answer = []
    i = 1
    a = 2 * i - 1    
    while a <= n:
        answer.append(a)
        i += 1
        a = 2 * i - 1
    return answer