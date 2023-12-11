# # 1326 폴짝폴짝
# import sys
# n = int(input())
# lst = list(map(int, sys.stdin.readline().split()))
# a, b = map(int, sys.stdin.readline().split())
# a -= 1 # index of lst
# b -= 1 # index of lst
# visited = [0 for _ in range(n)]
# bfs = []
# bfs.append(a)
# jumpcnt = 0 # jump count == depth
# while len(bfs) != 0 :
#     l = len(bfs)
#     jumpcnt += 1
#     # 너비 탐색
#     for i in range(l):
#         crnt = bfs.pop(0)
#         # n배 배수 노드(가지) 생성
#         for crntidx in range(crnt, n, lst[crnt]):
#             # if index 0~n를 벗어난다면 break, elif index b와 같다면 끝, else 자식 노드 추가
#             if 0 > crntidx or crntidx >= n : break
#             elif visited[crntidx]==0 and crntidx == b: # b에 도달하는 경우를 찾음
#                 print(jumpcnt)
#                 exit(0)
#             else:
#                 bfs.append(crntidx)
#                 visited[crntidx] = 1
#         for crntidx in range(crnt, n, -lst[crnt]):
#             # if index 0~n를 벗어난다면 break, elif index b와 같다면 끝, else 자식 노드 추가
#             if 0 > crntidx or crntidx >= n:
#                 break
#             elif visited[crntidx] == 0 and crntidx == b:  # b에 도달하는 경우를 찾음
#                 print(jumpcnt)
#                 exit(0)
#             else:
#                 bfs.append(crntidx)
#                 visited[crntidx] = 1
# print(-1)

# # 4963 섬의 개수
# import sys
# sys.setrecursionlimit(100)
# xi = [0, 0, 1, -1, -1, -1, 1, 1] # 각 자식
# yi = [1, -1, 0, 0, -1, 1, -1, 1]
#
# def dfs(x, y):
#     if x < 0 or x >= h or y < 0 or y >= w:
#         return False
#     if sea[x][y] == 1:
#         sea[x][y] = 0
#         for i in range(len(xi)):
#             dfs(x+xi[i], y+yi[i])
#         return True
#     return False
#
# while True:
#     w, h = map(int, sys.stdin.readline().split())
#     if w == 0 and h == 0:
#         break
#
#     sea = []
#     for _ in range(h):
#         sea.append(list(map(int, sys.stdin.readline().split())))
#
#     land = 0
#     for i in range(h):
#         for j in range(w):
#             if dfs(i, j) == True:
#                 land += 1
#     print(land)

# 2615 오목

# # 18353 병사 배치하기
# # dp 문제. 이중for문돌면서
# # j < i 인 상황에서 s[j] > s[i]일 떄 모두, max(dp[i], dp[j]+1) update 하기
# n = int(input())
# soldiers = list(map(int, input().split()))
# dp = [1] * n
#
# for i in range(1, n):
#     for j in range(i):
#         if soldiers[j] > soldiers[i]:
#             dp[i] = max(dp[i], dp[j]+1)
#
# print(n - max(dp))

# # 1912 연속합
# n = int(input())
# arr = list(map(int, input().split()))
# maxi = arr[0]
# for i in range(1, n):
#     if (arr[i-1] > 0):
#         arr[i] += arr[i-1]
#     maxi = max(arr[i], maxi)
# print(maxi)

# # 11053 가장 긴 증가하는 부분 수열
# n = int(input())
# seq = list(map(int, input().split()))
# dp = [0 for i in range(n)]
# dp[0]=1
# for i in range(n):
#     if (seq[i-1] < seq[i]):

# # 2630 색종이 만들기
# import sys
# n = int(input())
# paper = []
# for _ in range(n):
#     paper.append(list(map(int, sys.stdin.readline().strip().split())))
# wpaper = 0
# bpaper = 0
#
# def divfour(row, col, m):
#     global wpaper, bpaper
#     # 다 1인지 확인
#     blue, white = True, True
#     for i in range(row, row+m):
#         for j in range(col, col+m):
#             if paper[i][j] == 0:
#                 blue = False
#             if paper[i][j] == 1:
#                 white = False
#     print(row, col, m, blue, white)
#     # 섞임
#     if (blue or white) == False:
#         divfour(row, col, m // 2)
#         divfour(row+m//2, col, m // 2)
#         divfour(row, col+m//2, m // 2)
#         divfour(row+m//2, col+m//2, m // 2)
#     # 다 파란색
#     elif blue == True:
#         bpaper += 1
#     # 다 하얀색
#     else:
#         wpaper += 1
#
# r, c, m = 0, 0, n
# divfour(r, c, m)
#
# print(wpaper)
# print(bpaper)

# # 1780 종이의 개수
# import sys
# n = int(input())
# paper = []
# for _ in range(n):
#     paper.append(list(map(int, sys.stdin.readline().split())))
#
# pmone, pzero, pone = 0, 0, 0
#
# def divnine(row, col, m):
#     global pmone, pzero, pone
#     start = paper[row][col]
#     for i in range(row, row+m):
#         for j in range(col, col+m):
#             if paper[i][j] != start: # 시작과 다르다면 섞인것임
#                 divnine(row, col, m // 3)
#                 divnine(row, col + m // 3, m // 3)
#                 divnine(row, col + 2 * m // 3, m // 3)
#                 divnine(row + m // 3, col, m // 3)
#                 divnine(row + m // 3, col + m // 3, m // 3)
#                 divnine(row + m // 3, col + 2 * m // 3, m // 3)
#                 divnine(row + 2 * m // 3, col, m // 3)
#                 divnine(row + 2 * m // 3, col + m // 3, m // 3)
#                 divnine(row + 2 * m // 3, col + 2 * m // 3, m // 3)
#                 return
#     if start == -1: pmone += 1  # 다 -1
#     elif start == 0: pzero += 1 # 다 0
#     else: pone += 1             # 다 1
#
# r, c, m = 0, 0, n
# divnine(r, c, m)
#
# print(pmone)
# print(pzero)
# print(pone)

# # 2805 나무 자르기
# n, m = map(int,input().split())
# trees = list(map(int, input().split()))
#
# s, e = 0, max(trees)
# while(True):
#     sum = 0
#     cut = (s+e)//2
#     for t in trees:
#         sum += (t - cut) if t - cut > 0 else 0
#     if sum == m or s > e:
#         print(cut)
#         break
#     elif sum > m:
#         s = cut + 1
#     else:
#         e = cut - 1

# # 1654 랜선자르기
# k, n = map(int,input().split())
# wire = list()
# s, e = 1, 0
# for i in range(k):
#     wire.append(int(input()))
#     e = max(e, wire[i])
# # 이진탐색
# result = 0
# while(s <= e):
#     cnt = 0
#     lan = (s+e) // 2
#     for i in range(len(wire)):
#         cnt += wire[i] // lan
#     if cnt >= n:        # 원하는 수보다 (N) 더 많이 만들어지면 더 길게 해봄
#         result = max(result, lan)
#         s = lan + 1
#     else:               # 원하는 수에 못미치면 길이를 짧게 해봄
#         e = lan - 1
# print(result)

# # 16953 A->B
# A, B = map(int, input().split())
#
# def bfs(n):
#     queue = [n]
#     stage = 0
#     stop = False
#     while(queue):
#         if stop: break
#         stage += 1
#         cnt = len(queue)
#         for i in range(cnt):
#             tmp = queue.pop(0)
#             if tmp == B:
#                 stop = True
#                 break
#             if tmp * 2 <= B:
#                 queue.append(tmp*2)
#             if tmp*10+1 <= B:
#                 queue.append(tmp*10+1)
#
#     return stage if stop else -1
#
# print(bfs(A))

# # 15663 N과 M (9)
# import sys
# N, M = map(int, sys.stdin.readline().split())
# lst = sorted(list(map(int, sys.stdin.readline().split())))
# result = set()
# visited = [False for _ in range(N)]
#
# def backtrack(a, cnt):
#     if cnt == M:
#         if a not in result:
#             print(a[1:])
#             result.add(a)
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             backtrack(a + ' ' + str(lst[i]), cnt + 1)
#             visited[i] = False
#
# backtrack('', 0)

# # 1254 팰린드롬 만들기
# S = input()
#
# def palindrome(s):
#     l, r = 0, len(s) - 1
#     while(l < r):
#         if s[l] == s[r]:
#             l, r = l+1, r-1
#         else:
#             return False
#     return True
#
# for i in range(len(S)):
#     if palindrome(S[i:]):
#         print(len(S) + i)
#         break


# # 11053 가장 긴 증가하는 부분 수열
# n = int(input())
# A = list(map(int, input().split()))
#
# # dp[i] = i번째 원소를 마지막 원소로 하는 0~i 까지의 가장 긴 증가하는 부분 수열의 길이
# dp = [1] * n
#
# for i in range(n):
#     # 0~i 중에서 나(A[i])보다 작은 것들만 취하기
#     for j in range(i):
#         if A[i] > A[j]:
#             dp[i] = max(dp[j]+1, dp[i])
#
# print(max(dp))

