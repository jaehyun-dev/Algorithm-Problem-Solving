sm = ["'", ",", "-", ".", "?"]
while 1:
    flag1 = 0
    num = []
    while 1:
        a = input()
        if a == "*":
            break
        elif a == "#":
            flag1 = 1
            break
        cnt = 0
        flag2 = 0
        for i in range(len(a)):
            if a[i] == " ":
               flag2 = 1
               cnt += 1
            else:
                if flag2:
                    num.append(cnt)
                    flag2 = 0
                    cnt = 0
    num = list(map(lambda x:(x + 1) % 2, num))
    num += [0] * ((5 - len(num) % 5) % 5)
    enc_msg = []
    for i in range(len(num) // 5):
        temp = ""
        for j in range(5):
            temp += str(num[i * 5 + j])
        enc_msg.append(int(temp, 2))
    dec_msg = ""
    for i in enc_msg:
        if i == 0:
            dec_msg += " "
        elif i < 27:
            dec_msg += chr(i + 64)
        else:
            dec_msg += sm[i - 27]
    print(dec_msg)
    if flag1:
        break