def solution(price, money, count):
    diff = price * (((1 + count) * count) // 2) - money
    answer = diff if diff > 0 else 0

    return answer