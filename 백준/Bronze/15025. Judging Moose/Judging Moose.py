l, r = map(int, input().split())
if l == 0 and r == 0:
    print("Not a moose")
elif l == r:
    print(f"Even {2 * l}")
else:
    print(f"Odd {2 * max(l, r)}")