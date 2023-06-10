V = int(input())
vote = {"A":0, "B": 0}
for v in input():
    if v == "A":
        vote["A"] += 1
    else:
        vote["B"] += 1
if vote["A"] > vote["B"]:
    print("A")
elif vote["A"] < vote["B"]:
    print("B")
else:
    print("Tie")