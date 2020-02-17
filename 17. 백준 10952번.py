while (True):
    A, B = map(int, input().split())
    # map 함수는 두 문자를 동시에 정의할 때 사용한다. 여기서는 문자가 int함수로 인해 정수가 됨
    if A == 0 and B == 0:
        break
    else:
        print(A+B)