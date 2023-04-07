import sys
input = sys.stdin.readline
T = int(input())
val_dict = {"kg": 2.2046, "lb": 0.4536, "l": 0.2642, "g": 3.7854}
unit_dict = {"kg": "lb", "lb": "kg", "l": "g", "g": "l"}
for _ in range(T):
    val, unit = input().split()
    print(format(round(float(val) * val_dict[unit], 4), '.4f'), unit_dict[unit])