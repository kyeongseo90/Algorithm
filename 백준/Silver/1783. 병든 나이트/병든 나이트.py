N, M = map(int, input().split())
if N == 1:
    print(1)
elif N == 2: # 위아래로 1칸씩만 움직이는 것밖에 못 씀
    if M > 8:
        print(4)
    else:
        print((M-1) // 2 + 1)
elif M < 5: # 이동 횟수가 4번보다 적게 나오는 경우
    print(M)
elif M == 5:
    print(M-1)
else: # 이동 횟수가 4번 이상인 경우 -> 4가지 경우 사용 > 오른쪽으로 2칸가는 경우를 한번씩만 쓰기
    print(M-2)