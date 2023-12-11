# # 3182 한동이는 공부가 하기 싫어!
# n = int(input())
# df = [0,] # 1부터 n까지 선배의 대답
#
# for _ in range(n):
#     df.append(int(input()))
#
# def dfs(start, cnt):
#     visit[start] = True
#     cnt += 1
#     if df[df[start]] != 0 and visit[df[start]] == False:
#         cnt = dfs(df[start], cnt)
#     return cnt
#
# ans = 0
# max = 0
#
# for i in range(1, n+1):
#     visit = [False for _ in range(n+1)]
#     res = dfs(i, 0)
#     if res > max:
#         ans = i
#         max = res
#
# print(ans)

# # 1654 랜선 자르기
# k, n = map(int, input().split())
# lan = []
# for _ in range(k):
#     lan.append(int(input()))
#
# start, end = 1, max(lan)
# while start <= end:
#     mid = (start+end) // 2
#     sum = 0 # mid로 만들 수 있는 랜선 수
#     for l in lan:
#         sum += l // mid
#
#     if sum >= n:
#         start = mid + 1
#     else :
#         end = mid - 1
# print(end)

# # 1406 에디터
# import sys
#
# front = list(sys.stdin.readline())
# back = []
#
# m = int(sys.stdin.readline())
#
# for _ in range(m):
#     cmd = sys.stdin.readline().split()
#     if len(front)>0 and cmd[0]=='L':
#         back.append(front[len(front)-1])
#         front.pop()
#     elif len(back)>0 and cmd[0]=='D':
#         front.append(back[len(back)-1])
#         back.pop()
#     elif len(front)>0 and cmd[0]=='B':
#         front.pop()
#     elif cmd[0]=='P':
#         front.append(cmd[1])
#
# print(''.join(front+list(reversed(back))))
# # for f in front: print(f, end='')
# # for b in reversed(back): print(b, end='')

# # 11047 동전 0
# import sys
# n, k = map(int, sys.stdin.readline().split())
# coin = list()
# for i in range(n):
#     coin.append(int(sys.stdin.readline().strip()))
#
# ans = 0
# for div in reversed(coin):
#     tmp, k = divmod(k, div) # 몫, 나머지
#     ans += tmp
#
# print(ans)

# # 1449 수리공 항승
# import sys
# n, l = map(int, sys.stdin.readline().split())
# leaks = sorted(list(map(int, sys.stdin.readline().split())))
#
# ans = 0
# last_tape = 0
#
# for i in range(n):
#     if last_tape >= leaks[i] + 0.5: # 기존 tape으로 땜빵
#         continue
#     last_tape = leaks[i] - 0.5 + l # 새 tape 붙이기
#     ans += 1
#
# print(ans)

# # 1431 시리얼 번호
# import sys, re
# n = int(sys.stdin.readline())
# guitars = list()
# for serial in range(n):
#     guitars.append(sys.stdin.readline().strip())
#
# def serial_sort():
#     # 사전순 정렬
#     print(guitars)
#     guitars.sort()
#     print(guitars)
#
#     # 숫자 정렬
#     dct = {ser : 0 for ser in guitars} # value에 숫자합
#     for ser in dct:
#         nums = re.findall(r'\d', ser)
#         sum_num = 0
#         for i in nums:
#             sum_num += int(i)
#         dct[ser] = sum_num
#     sorted(dct.items(), key = lambda item: item[1])
#
#     # 길이 오름차순 정렬
#     for ser in dct:
#         num = len(ser)
#         dct[ser] = num
#     sorted(dct.items(), key = lambda item: item[1])
#
#     return dct
#
# sorted_dct = serial_sort()
#
# for ser in sorted_dct:
#     print(ser)

# # 15649 N과 M (1) - backtracking
# import sys
# n, m = map(int, sys.stdin.readline().split())
# lst = [0 for _ in range(9)]
# used = [False for _ in range(9)] # 중복 X
#
# def nCm(k):
#     if k == m:  # 길이 m 완성
#         for i in range(m):
#             print(lst[i], end=' ')
#         print()
#         return 0
#     for i in range(1, n+1): # 1부터 n까지
#         if not used[i]:
#             lst[k] = i
#             used[i] = True
#             nCm(k+1)    # 재귀
#             used[i] = False
#
# nCm(0)

# # 1966 프린터 큐
# import sys
# testcase = int(input())
# for _ in range(testcase):
#     # 각 테스트케이스 실행
#     N, M = map(int, sys.stdin.readline().split())
#     que = list(sys.stdin.readline().split())
#     cnt = 0
#     while True:
#         # 맨앞 값이 가장 큰 값이라면, 그냥 pop
#         if que[0]==max(que):
#             cnt += 1
#             que.pop(0)
#             # 위치 M 업데이트
#             if M==0:
#                 print(cnt)
#                 break
#             else: M -= 1
#         # 더 큰 값이 뒤에 존재한다면, pop 후 append
#         else:
#             que.append(que.pop(0))
#             # 위치 M 업데이트
#             if M == 0:  M = len(que)-1
#             else:       M -= 1

# # 15650 N과 M (2)
# # 이것이야말로 combination!
# # 1 combination 이용하기
# import sys
# from itertools import combinations
# n, m = map(int, sys.stdin.readline().split())
# lst = [i for i in range(1, n+1)]
# ans = list(combinations(lst, m))
# for a in ans:
#     print(*a)

# # 2 backtracking
# import sys
# lst = []
# n, m = map(int, sys.stdin.readline().split())
#
# def nCm(cnt):
#     if cnt == m:
#         for i in lst:
#             print(i, end=' ')
#         print()
#         return 0
#     for i in range(1 if len(lst) == 0 else lst[cnt-1]+1, n+1):
#         lst.append(i)
#         nCm(cnt+1)
#         lst.pop()
#
# nCm(0)

# # 2003 수들의 합 2
# import sys
# n, m = map(int, sys.stdin.readline().split())
# lst = list(map(int, sys.stdin.readline().split()))
# ans = 0
# left, right = 0, 0
#
# while left <= right and right <= n:
#     lsum = sum(lst[left:right])
#     if lsum == m:
#         ans += 1
#         right += 1
#     elif lsum < m:
#         right += 1
#     else:
#         left += 1
#
# print(ans)

# # 9507 Generations of Tribbles
# t = int(input())
# koong = [1, 1, 2, 4] # 꿍 피보나치
# for _ in range(t):
#     case = int(input())
#     if len(koong) <= case:
#         for i in range(len(koong), case+1):
#             koong.append(sum(koong[i-4:i]))
#     print(koong[case])

# # 1904 01타일
# mod = 15746
# n = int(input())
# dp = [0, 1, 2] # dp[1]=1, dp[2]=2
# for i in range(3, n+1):
#     dp.append((dp[i-2]+dp[i-1])%mod)
# print(dp[n])

# n, m = map(int, input().split())
# arr = [True] * (m + 1)
# k = (int)(m**0.5)
# for i in range(2, k+1):
#     if arr[i] == True:
#         for j in range(i+1, m):
#             if j%i == 0:
#                 arr[j] = False
# for i in range(n, m):
#     if arr[i] == True:
#         print(i)


# def isPrime(num):
#     if num==1: return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0: return False
#         return True
#
# M, N = map(int, input().split())
# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)

# # 14425 문자열 집합
# n, m = map(int, input().split())
# s = set()
# for _ in range(n):
#     s.add(input())
# cnt = 0
# for _ in range(m):
#     if (input() in s):
#         cnt+=1
# print(cnt)

# # 11478 서로 다른 부분 문자열의 개수
# str = input()
# subset = set()
# length = len(str)
# for i in range(1, length+1):
#     for j in range(length):
#         subset.add(str[j:j+i])
# print(len(subset))

# # 15651 N과 M (3)
# n, m = map(int, input().split())
# answer = []
#
# def bt(): # backtracking
#     if len(answer) == m:
#         print(' '.join(map(str, answer)))
#         return
#     for i in range(1, n+1):
#         answer.append(i)
#         bt()
#         answer.pop()
# bt()

# # 15652 N과 M (4)
# n, m = map(int, input().split())
# answer = []
#
# def bt(end): # backtracking
#     if len(answer) == m:
#         print(' '.join(map(str, answer)))
#         return
#
#     for i in range(end, n+1): # 비내림차순을 위한 범위 지정
#         answer.append(i)
#         bt(i)
#         answer.pop()
# bt(1)

# # 9461 파도반 수열
# t = int(input())
# padovan = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
# tmp = 10
# for i in range(t):
#     n = int(input())
#     if (tmp < n):
#         for j in range(tmp+1, n+1):
#             padovan.append(padovan[j-2] + padovan[j-3])
#             tmp = j
#     print(padovan[n])

# # 2579 계단 오르기
# # *_*
# # **_*
# n = int(input())
# stair = []
# dp = [0 for i in range(n+1)]
# for i in range(n):
#     stair.append(int(input()))
# # exception
# if n == 1:
#     print(stair[0])
#     exit(0)
# elif n == 2:
#     print(stair[0]+stair[1])
#     exit(0)
# # init
# dp[n-1] = stair[n-1]
# dp[n-2] = stair[n-1] + stair[n-2]
# dp[n-3] = stair[n-1] + stair[n-3]
# # dynamic programming
# for i in range(n-4, -1, -1):
#     dp[i] = max(stair[i] + dp[i+2], stair[i] + stair[i+1] + dp[i+3])
# print(max(dp[0], dp[1]))

# # 1463 1로 만들기
# x = int(input())

# # 11659 구간 합 구하기
# import sys
# n, m = map(int, sys.stdin.readline().split())
# lst = list(map(int, sys.stdin.readline().split()))
# slst = [0]
# for i in range(n):
#     slst.append(lst[i] + slst[i])
# for _ in range(m):
#     i, j = map(int, sys.stdin.readline().split())
#     print(slst[j]-slst[i-1])

# # 2559 수열
# n, k = map(int, input().split())
# temp = list(map(int, input().split()))
# sum, maxi = 0, 0
# l = 0
# for i in range(k): sum += temp[i]
# maxi = sum
# for r in range(k, n):
#     sum += temp[r] - temp[l]
#     if sum > maxi: maxi = sum
#     l += 1
# print(maxi)

# # 13305 주유소
# # 처음도시에서 길을 가는 주유 가격을 더하고,
# # 해당 가격을 저장해둔 후, 다음 지역에서의 가격과 비교하여 더 저렴한 가격으로 다음 길을 간다.
# # 이런식으로 계속 가다보면 가장 저렴하게 갈 수 있음.
# n = int(input())
# road = list(map(int, input().split()))
# price = list(map(int, input().split()))
#
# total = price[0] * road[0]
# lowest = price[0]
# for i in range(1, n-1):
#     lowest = min(lowest, price[i])
#     total += road[i] * lowest
# print(total)

# # 1966 프린터 큐
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# while(n):
#     a, b = map(int, sys.stdin.readline().strip().split())
#     lst = list(map(int, sys.stdin.readline().strip().split()))
#     declst = deque(sorted(lst, reverse=True))
#     q = deque()
#     for i in lst:
#         q.append([i, 0])
#     q[b][1] = 1
#     cnt = 1
#
#     while(True):
#         if (q[0][0] == declst[0]):
#             if (q[0][1] == 1):
#                 print(cnt)
#                 break
#             q.popleft()
#             declst.popleft()
#             cnt += 1
#         else:
#             q.append(q.popleft())
#
#     n-=1

# # 1021 회전하는 큐
# # 근데 이 방법보다 더 적게 풀 수 있는 방법이 있지 않나?
# # 만약 앞으로도 내가 뽑아야 할 게 지금 앞에 없으면 1번 연산 계속 하면 되는거 아냐?
# import sys
# from collections import deque
# n, m = map(int, sys.stdin.readline().strip().split())
# pick = list(map(int, sys.stdin.readline().strip().split()))
# dq = deque(i for i in range(1, n+1))
#
# cnt = 0
# while(pick):
#     loc = dq.index(pick[0])
#     # 맨 앞에 뽑아야 하는게 있으면 뽑기. count X
#     if dq[0] == pick[0]:
#         dq.popleft()
#         pick.pop(0)
#     # 왼쪽 이동이 오른쪽 이동보다 더 짧으면 이동. count O
#     elif loc <= len(dq) - loc:
#         for _ in range(loc): dq.append(dq.popleft())
#         cnt += loc
#     # 오른쪽 이동이 더 짧을 경우. count O
#     else:
#         for _ in range(len(dq)-loc): dq.appendleft(dq.pop())
#         cnt += len(dq)-loc
# print(cnt)

# # 4779 칸토어 집합
# def recursion(n):
#     if n == 1:
#         print("- -", end='')
#     else:
#         recursion(n-1)
#         for i in range(pow(3, n-1)): print(" ", end='')
#         recursion(n-1)
#     n-=1
#
# while(True):
#     try:
#         n = int(input())
#         if n == 0: print("-")
#         else:
#             recursion(n)
#             print("")
#     except EOFError:
#         break

# # 1213 팰린드롬 만들기
# alphabet = [0] * 26
# palin = input()
# for c in palin: alphabet[ord(c)-65] += 1
#
# discm = 1 if len(palin) % 2 == 1 else 0
# result, midchr = "", ""
# for i in range(len(alphabet)):
#     if alphabet[i] > 1:
#         for j in range(alphabet[i]//2):
#             result += chr(i + 65)
#         alphabet[i] -= (alphabet[i] // 2) * 2
#     if alphabet[i] == 1:
#         midchr = chr(i + 65)
#         discm -= 1
#         if discm < 0:
#             print("I'm Sorry Hansoo")
#             exit(0)
#
# opposite = result[::-1]
# print(result+opposite if len(palin) % 2 != 1 else result+midchr+opposite)
