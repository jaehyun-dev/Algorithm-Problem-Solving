N = int(input())
for _ in range(N):
    p = input()
    if p == "P=NP":
        print("skipped")
    else:
        exec(f"print({p})")