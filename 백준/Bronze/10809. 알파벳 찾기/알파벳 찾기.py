n = input()
for i in range(97, 123):
    if chr(i) in n:
        print(n.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')
        

# asdz9908님의 
s = list(input())    #리스트에 입력 값 저장
d = {}    #저장할 딕셔너리 초기화

for i in s:    #입력받은 리스트 길이만큼 반복
    if i not in d:    #딕셔너리에 i번째 인덱스가 
        d[i] = s.index(i)    #없으면 추가
    else:    #아니면
        pass    #통과
alpha = "abcdefghijklmnopqrstuvwxyz"    #비교할 알파벳 저장
    
for i in alpha:    #알파벳 길이만큼 반복
    if i in d:    #만약 알파벳이 딕셔너리에 있다면
        print(d[i], end= " ")    #해당 위치값을 출력
    else:
        print(-1, end=" ")    #없으면 -1 출력
