while 1:
    a = input().split()
    if not int(a[0]):
        break
    s = int(a[0])
    ad = a[1]
    b = set()
    wa = set()
    cnt = 0
    for i in ad:
        if i not in b and i not in wa:
            if len(b) < s:
                b.add(i)
            else:
                wa.add(i)
        else:
            if i in b:
                b.remove(i)
            if i in wa:
                wa.remove(i)
                cnt += 1
    if not cnt:
        print("All customers tanned successfully.")
    else:
        print(f"{cnt} customer(s) walked away.")