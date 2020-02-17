N = int(input())
# input함수를 int함수로 감싸줌으로써 입력받은 값을 문자형에서 정수형으로 형변환해준다.
for i in range(1, N+1):
    # 1~N까지
    print("*"*i)
    # 별을 i번 반복하여 출력한다.