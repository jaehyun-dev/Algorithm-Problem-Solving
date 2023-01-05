import sys
i = 1
for line in sys.stdin:
    if line.strip() == "0":
        break
    print(f"Case {i}: Sorting... done!")
    i += 1