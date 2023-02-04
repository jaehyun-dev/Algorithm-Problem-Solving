team = []
for _ in range(2):
    score = 0
    for i in [3, 2, 1]:
        score += int(input()) * i
    team.append(score)
if team[0] > team[1]:
    print("A")
elif team[0] < team[1]:
    print("B")
else:
    print("T")