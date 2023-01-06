a = list(map(int, input().split()))
b = list(map(int, input().split()))
score = [6, 3, 2, 1, 2]
a_score = 0
b_score = 0
for i in range(5):
    a_score += a[i] * score[i]
    b_score += b[i] * score[i]
print(a_score, b_score)