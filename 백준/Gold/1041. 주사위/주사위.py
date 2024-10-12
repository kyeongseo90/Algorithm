import sys
input = sys.stdin.readline

ans = 0

N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    dice.sort()
    for i in range(5):
        ans += dice[i]
else:
    # 주사위 한 면의 최솟값
    one_side = min(dice)

    # 주사위 두 면의 최솟값
    # AB, AC, AD, AE, BC, BD, BF, CE, CF, DE, DF, EF : 12개
    # 12, 13, 14, 15, 23, 24, 26, 35, 36, 45, 46, 56
    # 1-6 | 2-5 | 3-4 => 0-5, 1-4, 2-3 

    two_side = sum(dice)
    for i in range(6):
        for j in range(i+1, 6):
            if i+j != 5 and i != j:
                two_side = min(two_side, dice[i]+dice[j])

    # 주사위 세 면의 최솟값
    # ABC, ABD, ACE, ADE, BCF, BDF, CEF, DEF
    # 123, 124, 135, 145, 236, 246, 346, 456
    three_side = min(dice[0] + dice[1] + dice[2],
                     dice[0] + dice[1] + dice[3],
                     dice[0] + dice[2] + dice[4],
                     dice[0] + dice[3] + dice[4],
                     dice[1] + dice[2] + dice[5],
                     dice[1] + dice[3] + dice[5],
                     dice[2] + dice[4] + dice[5],
                     dice[3] + dice[4] + dice[5])

    ans += one_side * ((N-2) ** 2 + (N-2) * (N-1) * 4)
    ans += two_side * ((N-2) * 4 + (N-1) * 4)
    ans += three_side * 4

print(ans)