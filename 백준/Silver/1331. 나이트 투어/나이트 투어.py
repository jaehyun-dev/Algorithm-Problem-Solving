a = input()
c_p = ord(a[0])
r_p = int(a[1])
i = 1
visited = []
visited.append((c_p, r_p))
flag = True
while i < 36:
    a = input()
    c_c = ord(a[0])
    r_c = int(a[1])
    if (c_c, r_c) in visited:
        flag = False
        break
    else:
        if (abs(c_p - c_c) == 1 and abs(r_p - r_c) == 2) or (abs(c_p - c_c) == 2 and abs(r_p - r_c) == 1):
            c_p = c_c
            r_p = r_c
            visited.append((c_p, r_p))
            i += 1
        else:
            flag = False
            break

if flag:
    first = visited[0]
    last = visited[35]
    if not ((abs(first[0] - last[0]) == 1 and abs(first[1] - last[1]) == 2) or (abs(first[0] - last[0]) == 2 and abs(first[1] - last[1]) == 1)):
       flag = False

print('Valid' if flag else 'Invalid')