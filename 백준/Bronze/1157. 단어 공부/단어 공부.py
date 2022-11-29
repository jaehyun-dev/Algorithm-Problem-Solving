word = input()
cap = word.upper()
dic = {}

for i in range(len(cap)):
    if cap[i] not in dic:
        dic[cap[i]] = 1
    else:
        dic[cap[i]] += 1

sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

if (len(sorted_dic) > 1 and list(sorted_dic.values())[0] != list(sorted_dic.values())[1]) or len(sorted_dic) == 1:
    print(list(sorted_dic)[0])
else:
    print("?")