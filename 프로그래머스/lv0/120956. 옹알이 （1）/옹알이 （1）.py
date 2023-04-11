def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        a = i
        for p in pron:
            a = a.replace(p, " ")
        if a.rstrip() == "":
            answer += 1
    return answer