N = int(input())
bigBag = N // 5
smallBag = (N-5*bigBag) // 3
while bigBag * 5 + smallBag * 3 != N and bigBag >= 0:
    bigBag -= 1
    smallBag = (N-5*bigBag) // 3
if bigBag < 0:
    print(-1)
else:
    print(bigBag+smallBag)