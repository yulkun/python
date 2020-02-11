a=input().split(' ')  #split()이라고만 해도 띄어쓰기로 분류된다.
A=int(a[0])
B=int(a[1])
if A>B:
    print('>')
else:
    if A<B:
        print('<')
    else:
        print('==')