import sys
for line in sys.stdin:
    if line.strip() == "# 0 0":
        break
    a = list(line.strip().split())
    print(a[0], 'Senior' if (int(a[1]) > 17 or int(a[2]) >= 80) else 'Junior')