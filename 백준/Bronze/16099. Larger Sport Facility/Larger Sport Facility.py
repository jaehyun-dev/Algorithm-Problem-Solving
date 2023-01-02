n = int(input())
for _ in range(n):
    i_t, w_t, i_e, w_e = map(int, input().split())
    a_t = i_t * w_t
    a_e = i_e * w_e
    if a_t > a_e:
        print("TelecomParisTech")
    elif a_t < a_e:
        print("Eurecom")
    else:
        print("Tie")