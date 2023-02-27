X = int(input())
count = 1
poles = [64]
while sum(poles) > X:
    shortest = sorted(poles)[0]
    poles.remove(shortest)
    for _ in range(2):
        poles.append(shortest // 2)
    if sum(sorted(poles)[1:]) >= X:
        poles.remove(sorted(poles)[0])
print(len(poles))