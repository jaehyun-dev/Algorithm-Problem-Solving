def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        answer.append(sorted(emergency, reverse=True).index(emergency[i]) + 1)
    return answer