a = input()
if a[0] == '"' and a[-1] == '"':
    if a[1:-1].strip() == "":
        print("CE")
    else:
        print(a[1:-1])
else:
    print("CE")