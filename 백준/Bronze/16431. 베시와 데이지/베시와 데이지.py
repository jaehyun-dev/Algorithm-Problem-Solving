br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())
bd = max(abs(br - jr), abs(bc - jc))
dd = abs(dr - jr) + abs(dc - jc)
if bd < dd:
    print("bessie")
elif dd < bd:
    print("daisy")
else:
    print("tie")