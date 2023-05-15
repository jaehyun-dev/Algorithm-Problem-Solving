T = int(input())
i = 0
while i < T:
    a = int(input())
    if a == 1:
        print("#")
    elif a == 2:
        print("##\n##")
    else:
        print("#" * a)
        for _ in range(a - 2):
            print(f"#{'J' * (a - 2)}#")
        print("#" * a)
    i += 1
    if i < T:
        print()