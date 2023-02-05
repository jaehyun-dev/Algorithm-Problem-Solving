a = list(map(int, input().split()))
b = ["Soongsil", "Korea", "Hanyang"]
if sum(a) > 99:
    print("OK")
else:
    print(b[a.index(min(a))])