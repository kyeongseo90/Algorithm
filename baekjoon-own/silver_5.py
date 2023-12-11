# # dk
# import sys
#
# n = int(input())
# narr = set(sys.stdin.readline().strip().split())
# m = int(input())
# marr = sys.stdin.readline().strip().split()
#
# for i in marr:
#     print(1) if i in narr else print(0)

# # 2204 도비의 난독증 테스트
# while True:
#     n = int(input())
#     if n == 0: break # last input 0
#
#     word = []
#     for i in range(n):
#         word.append(input())
#
#     word.sort(key=str.lower) # key값을 기준으로 정렬, default 오름차순.
#     print(word[0])

# # 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# #1
# import sys
#
# line = sys.stdin.readline().strip().split()
# n = int(line[0])
# m = int(line[1])
# s = set()
# tmp = set()
#
# if n < 4:
#     print(0)
#     exit()
#
# for _ in range(m):
#     p, q = sys.stdin.readline().strip().split()
#
#     for i in range(1, n+1):
#         tmp.add(int(p))
#         tmp.add(int(q))
#         tmp.add(i)
#         if len(tmp) == 3:
#             sorted(tmp)
#             # print(tmp)
#             s.add(tuple(tmp))
#         tmp.clear()
#
# print(int(n*(n-1)*(n-2)/6 - len(s)))

# 2508 사탕 박사 고창영
# for _ in range(int(input())):
#     input()
#     row, col = map(int, input().split())
#     candy = 0
#     arr = [] # 2차원배열
#     for _ in range(row):
#         arr += input().split()
#
#     for i in range(row):
#         for j in range(col):
#             if arr[i][j] == 'o' : # 즉 사탕일시
#                 # 가로 >o<
#                 if 0 < j < col-1 and arr[i][j-1] == '>' and arr[i][j+1] == '<':
#                     candy+=1
#                 # 세로 vo^
#                 if 0 < i < row-1 and arr[i-1][j] == 'v' and arr[i+1][j] == '^':
#                     candy+=1
#
#     print(candy)

# # 11650 좌표 정렬하기
# n = int(input())
# list = []
# for _ in range(n):
#     i, j = map(int, input().split())
#     list.append([i, j])
#
# sorted_list = sorted(list)
#
# for i in range(n):
#     print(sorted_list[i][0], sorted_list[i][1])

# # 7568 덩치
# n = int(input())
# size = []
# for i in range(n):
#     size.append(list(map(int, input().split())))
# cnt = 1
# result = []
# for i in range(n):
#     cnt = 1
#     for j in range(n):
#         if (i!=j and size[i][0]<size[j][0] and size[i][1]<size[j][1]):
#             cnt += 1
#     result.append(cnt)
# print(*result)

# # 1436 영화감독 숌
# n = int(input())
# num = 0
# while(n):
#     num += 1
#     if "666" in str(num):
#         n -= 1
# print(num)

# # 11866 요세푸스 문제 0
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().strip().split())
# Josephus = deque([i for i in range(1, n+1)])
# ans = []
# delete = 0
# while(Josephus):
#     delete = (delete+k-1) % len(Josephus) # delete index update
#     ans.append(Josephus[delete])        # add answer(Josephus permutation)
#     Josephus.remove(Josephus[delete])   # remove
# print("<", end='')
# print(', '.join(list(map(str, ans))), end='')
# print(">", end='')

# # 2740 행렬 곱셈
# import sys
# A = []
# n, m = map(int, sys.stdin.readline().strip().split())
# for i in range(n):
#     A.append(list(map(int, sys.stdin.readline().strip().split())))
# B = []
# m, k = map(int, sys.stdin.readline().strip().split())
# for i in range(m):
#     B.append(list(map(int, sys.stdin.readline().strip().split())))
# C = [[0 for _ in range(k)] for _ in range(n)]
# for i in range(n):
#     for j in range(k):
#         for p in range(m):
#             C[i][j] += A[i][p] * B[p][j]
#
# for i in C:
#     print(' '.join(map(str,i)))

