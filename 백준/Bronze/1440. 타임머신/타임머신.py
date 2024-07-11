import itertools
t = list(map(int, input().split(":")))
cnt = 0
for i in itertools.permutations(t, 3):
    HH, MM, SS = i
    if 0 < HH <= 12 and 0 <= MM < 60 and 0 <= SS < 60:
        cnt += 1
print(cnt)