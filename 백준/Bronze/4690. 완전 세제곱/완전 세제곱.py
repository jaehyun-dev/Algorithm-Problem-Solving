import itertools
comb = itertools.product(*[range(1, 101) for n in [0, 0, 0, 0]])
for case in comb:
    a, b, c, d = case
    if a >= d and b <= c <= d and a ** 3 == b ** 3 + c ** 3 + d ** 3 and b > 1:
        print(f"Cube = {a}, Triple = ({b},{c},{d})")