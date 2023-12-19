cost = {"Paper": 57.99,
        "Printer": 120.50,
        "Planners": 31.25,
        "Binders": 22.50,
        "Calendar": 10.95,
        "Notebooks": 11.20,
        "Ink": 66.95}

cnt = 0
while 1:
    a = input().strip()
    if a == "EOI":
        break
    cnt += cost[a]

print(f"${cnt:.2f}")