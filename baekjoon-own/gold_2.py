# 11444 피보나치 수 6

# # 1300 K번째 수
# n, k = int(input()), int(input())
# s, e = 1, k
# while(s<=e):
#     mid = (s+e) // 2
#     tmp = 0
#     for i in range(1, n+1):
#         tmp += min(mid//i, n)
#         # 각 행마다 mid보다 작은 수의 개수를 더해줌 => '기준 수'를 '행'으로 나눈 몫
#         # (mid//i는 mid를 행으로 나눈 몫, min은 N*N이므로 N을 초과할 수 없어서)
#     if tmp >= k:
#         ans = mid
#         e = mid - 1
#     else:
#         s = mid + 1
# print(ans)

# # 12015 가장 긴 증가하는 부분 수열 2
# n = int(input())
# A = list(map(int, input().split()))
# lst = [0]
# for a in A:
#     if lst[-1] < a:
#         lst.append(a)
#     else:
#         s, e = 0, len(lst)
#         while(s<=e):
#             mid = (s+e)//2
#             if lst[mid] < a:
#                 s = mid+1
#             else:
#                 e = mid-1
#         lst[e] = a
# print(len(lst)-1)


# # 1167 트리의 지름
# import sys
# n = int(sys.stdin.readline())
#
# branch = [[] for i in range(n+1)]
#
# tmp = []
# for i in range(n):
#     tmp = list(map(int, sys.stdin.readline().split()))
#     pst = tmp[0]
#     for j in range(1, len(tmp)-2, 2):
#         branch[pst].append((tmp[j], tmp[j + 1]))
#
# # x 에서 가장 긴 노드를 찾기
# def mostlongtrace(x):
#
#     resNode, resLen = 0, 0
#     visited = [False for _ in range(n+1)]
#
#     # (이전 노드, 누적 길이)
#     que = [(x, 0)]
#
#     # bfs
#     while que:
#         connect, curlen = que.pop(0)
#         visited[connect] = True
#
#         # 가중치를 구하는 문제이므로 몇 번 거쳐서 갔는지(depth) 계산 안해도 됨 -> for문 하나X
#         # 갈 수 있는 경로 탐색 -> que에 삽입
#         for i, weight in branch[connect]: # (connect, i) in branch and
#             if not visited[i]:
#                 tmpsum = curlen+weight
#                 que.append((i, tmpsum))                     # que에 다음 경로 추가
#                 visited[i] = True                           # i 노드 visited 처리
#                 # 경로 하나 추가할 때마다 resNode,resLen MAX로 업데이트
#                 if resLen <= tmpsum:
#                     resLen = tmpsum
#                     resNode = i
#     # return 가장 긴 노드, 해당 노드까지의 길이
#     return resNode, resLen
#
# print(mostlongtrace(mostlongtrace(1)[0])[1])