# import math
# N = int(input())
# lucky = 0
# len = int(math.log10(N))+1
# for i in range(len):
#     num = int(N % math.pow(10, i+1) / math.pow(10, i))
#     if i < len/2:
#         lucky += num
#     else:
#         lucky -= num
# print("LUCKY" if lucky == 0 else "READY")

# import operator
# def solution(N, stages):
#     d = {i+1: 0 for i in range(N+1)}
#     # 입력
#     for i in stages: d[i]+=1
#     pp = 0
#     # 실패율 계산
#     for i in range(N+1, 0, -1):
#         pp += d[i]
#         if (pp != 0): d[i]= d[i]/pp
#     d.pop(N+1)
#     ans = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
#     answer = []
#     for i in ans:
#         answer.append(i[0])
#     return answer
#
# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# print(solution(N, stages))

# # 2798 블랙잭
# import itertools, math
# n, m = map(int, input().split())
# cards = list(map(int, input().split()))
# arr = list(itertools.combinations(cards, 3))
# result = 0
# for i in range(len(arr)):
#     tmp = math.fsum(arr[i])
#     if tmp <= m:
#         result = max(result, tmp)
# print(int(result))

# # 2231 분해합
# n = int(input())
# result = 0
# for i in range(n):
#     tmp = i
#     stri = str(i)
#     for x in stri:
#         tmp += int(x)
#     if tmp == n:
#         result = i
#         break
# print(result)

# # 24416 알고리즘 수업 - 피보나치 수 1
# # 2 -> 1 0
# # 3 -> 2 1
# # 4 -> 3 2
# # 5 -> 5 3
# # 6 -> 8 4
# # 7 -> 13 5
# # 8 -> 21 6
# # 9 -> 34 7
# def fibonacci(n):
#     global cnt
#     f[1] = 1
#     f[2] = 1
#     for i in range(3, n+1):
#         cnt += 1
#         f[i] = f[i-1]+f[i-2]
#     return f[n]
#
# n = int(input())
# f = [0] * (n+1)
#
# cnt = 0
# print(fibonacci(n), cnt) # cnf) cnt = n-2

# # 27433 팩토리얼 2
# import sys
# n = int(sys.stdin.readline())
# res = 1
# while(n):
#     res *= n
#     n-=1
# print(res)