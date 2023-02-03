import math
A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())
print("Whole pizza" if (R1 ** 2 * math.pi / P2) > (A1 / P1) else "Slice of pizza")