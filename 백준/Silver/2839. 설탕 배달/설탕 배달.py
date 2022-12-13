n = int(input())
bag_5 = n // 5
flag = True
while bag_5 >= 0:
    bag_3 = (n - (5 * bag_5)) // 3
    if (n - (5 * bag_5)) % 3 != 0:
        bag_5 -= 1
    else:
        print(bag_5 + bag_3)
        flag = False
        break

if flag:
    print(-1)