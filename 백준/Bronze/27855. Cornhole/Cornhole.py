H1, B1 = map(int, input().split())
H2, B2 = map(int, input().split())
s1 = H1 * 3 + B1
s2 = H2 * 3 + B2
if s1 > s2:
    print(1, s1 - s2)
elif s1 < s2:
    print(2, s2 - s1)
else:
    print("NO SCORE")