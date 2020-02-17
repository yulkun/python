T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1, A, B, A+B))
    # format 함수는 앞에 형식을 적어준 후 괄호 뒤에 쓰여져야하는 숫자들을 적어준다.