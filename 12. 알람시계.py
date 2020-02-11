H, M = map(int, input().split())
# map함수는 똑같은 함수 쓸때 사용
# H, M 모두 정수이므로 int함수 사용
# split 함수로 H와 M을 띄어쓰기로 구분

if M>44:
    print(H, M-45)
elif H>0 and M<45:
    print(H-1, M+15)
# elif: if가 아닌 경우
else:
    print(23, M+15)
#else: elif와 if 모두 아닌 경우

# int함수를 썼으므로 print가로안에 ""는 쓰지 않는다.
