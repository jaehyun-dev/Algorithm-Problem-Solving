p1, q1, p2, q2 = map(int, input().split())
area = p1/q1 * p2/q2 * 1/2
print(1 if area == int(area) else 0)