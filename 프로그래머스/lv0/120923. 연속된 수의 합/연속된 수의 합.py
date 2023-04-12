def solution(num, total):
    answer = []
    a = (-(num ** 2) + num + 2 * total) // (2 * num)
    for i in range(num):
        answer.append(a + i)
    return answer