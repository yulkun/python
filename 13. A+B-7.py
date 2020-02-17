import sys
# input 함수로 했더니 런타임시간을 잡아먹어서 바꿔줌
read = sys.stdin.readline

T = int(read())

for i in range(T):
    ab = [int(x) for x in read().split()]
    print("Case #{}: {}".format(i+1, ab[0]+ab[1]))

    # "#"이 있는 경우 설명문으로 간주되므로 큰 따옴표를 통해 입력될 수 있도록 구분한다.