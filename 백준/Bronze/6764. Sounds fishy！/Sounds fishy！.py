a = []
for _ in range(4):
    a.append(int(input()))
if len(set(a)) == 1:
    print("Fish At Constant Depth")
elif len(set(a)) == 4:
    if a == sorted(a):
        print("Fish Rising")
    elif a == sorted(a, reverse=True):
        print("Fish Diving")
    else:
        print("No Fish")
else:
    print("No Fish")