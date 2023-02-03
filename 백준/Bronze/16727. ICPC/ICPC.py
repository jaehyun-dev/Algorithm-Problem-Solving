p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
p = p1 + p2
s = s1 + s2
if p > s:
    print("Persepolis")
elif p < s:
    print("Esteghlal")
else:
    if p2 > s1:
        print("Persepolis")
    elif p2 < s1:
        print("Esteghlal")
    else:
        print("Penalty")