n = int(input())
for _ in range(n):
    quiz = input()
    i = 0
    score = 0
    count = 0
    while i < len(quiz):
        if quiz[i] == 'O':
            count += 1
        else:
            count = 0
        score += count
        i += 1
    print(score)