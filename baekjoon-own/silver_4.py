# #11866 요세푸스 문제 0
# n, k = map(int, input().split())
#
# cir = [i for i in range(1, n+1)]
#
# print('<', end='')
# m = 0
# while len(cir) > 1 :
#     m = (m+k-1) % len(cir)
#     print(cir[m], end=', ')
#     cir.remove(cir[m])
# print(cir[0], end='>')

# # 1487 물건 팔기
# n = int(input())
# profit = []
# maxp = -1
# for i in range(n):
#     t1, t2 = map(int, input().split())
#     profit.append([t1,t2]) #
#     if maxp < t1-t2:
#         maxp = t1-t2
#
# if maxp <= 0:
#     print(0)
#     exit(0)

# # 10815 숫자카드
# n = int(input())
# fulltime = list(map(int, input().split())) # 상근
# fulltime.sort()
# m = int(input())
# cardset = list(map(int, input().split()))
#
# def binary(start, end, f):
#     while start<=end:
#         mid = (start+end)//2
#         if fulltime[mid] == f:
#             return end
#         elif fulltime[mid] < f:
#             start = mid+1
#         else:
#             end = mid-1
#     return None
#
# for card in cardset:
#     if binary(0, n-1, card) is not None:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# # 10825 국영수 / 정렬
# import sys
# n = int(input())
# grades = []
# for _ in range(n):
#     name, k, m, e = map(str, sys.stdin.readline().split())
#     grades.append([name, int(k), int(m), int(e)])
#
# grades.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
#
# for g in grades:
#     print(g[0])

# # 1049 기타줄 /
# import sys, math
# n, m = map(int, sys.stdin.readline().split())
# six, one = 1000, 1000
# for _ in range(m):
#     t1, t2 = map(int, sys.stdin.readline().split())
#     six = min(six, t1)
#     one = min(one, t2)
#
# if one * 6 <= six:
#     print(one * n)
# elif one * (n % 6) > six:
#     print(math.ceil(n / 6) * six)
# else:
#     print((n // 6) * six + (n % 6) * one)

# # 11656 접미사 배열
# import sys
# baekjoon = sys.stdin.readline()
# s = set()
# last = len(baekjoon)-1 # slicing을 위한 last index값
# for i in range(last):
#     s.add(baekjoon[i:last]) # slicing string
# lst = sorted(list(s)) # 리스트에 넣고 정렬
# for tail in lst:
#     print(tail)

# # 1543 문서 검색
# import sys
# str = sys.stdin.readline()
# fnd = sys.stdin.readline().strip()
# lenf = len(fnd)
# answer = 0
# cnt = 0 # to avoid duplication
#
# for i in range(len(str)-lenf):
#     if cnt != 0: # 건너뛰기
#         cnt-=1
#         continue
#
#     if str[i:i+lenf] == fnd: # same
#         answer+=1
#         i += lenf
#         cnt = lenf-1
#
# print(answer)

# # 1913 달팽이
# import sys
# n = int(sys.stdin.readline())
# fnd = int(sys.stdin.readline())
# snail = [[0 for _ in range(n)] for _ in range(n)]
#
# # (x, y) 시작 좌표
# x = n//2
# y = n//2
# num = 1     # 1 ~ n*n 까지
# len = 1     # dx,dy방향으로 가는 길이
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# xi, yi = 0, 0
# while True:
#     for _ in range(2):
#         for _ in range(len):
#             print(x, y)
#             snail[x][y] = num
#             if num == fnd:
#                 ans = [x+1, y+1]
#             elif num == n*n:
#                 break
#             x += dx[xi % 4]
#             y += dy[yi % 4]
#             num+=1
#         xi += 1
#         yi += 1
#         if num == n * n:
#             break
#     len+=1
#     if num == n * n:
#         break
#
# for i in range(n):
#     print(*snail[i])
#
# print(ans[0], ans[1])

# # 1018 체스판 다시 칠하기
# def make_chess_board(x, y):
#     WB = ['W', 'B']
#     BW = ['B', 'W']
#     case1, case2 = 0, 0
#     for i in range(8):
#         tmp1, tmp2 = 0, 0
#         for j in range(8):
#             if WB[j%2] != board[i+x][j+y]:
#                 tmp1 += 1
#             elif BW[j%2] != board[i+x][j+y]:
#                 tmp2 += 1
#         if (i%2 == 0):
#             case1 += tmp1
#             case2 += tmp2
#         else:
#             case1 += tmp2
#             case2 += tmp1
#     return min(case1, case2)
#
# n, m = map(int, input().split())
# board = []
# for i in range(n):
#     board.append(input())
# result = 64
# for i in range(n-7):
#     for j in range(m-7):
#         result = min(result, make_chess_board(i, j))
# print(result)

# # 1620 나는야 포켓몬 마스터 이다솜
# n, m = map(int, input().split())
# pocketmon = dict()
# for i in range(n):
#     tmp = input()
#     pocketmon[i+1] = tmp # 1 부터 ...
#     pocketmon[tmp] = i+1
# for _ in range(m):
#     tmp = input()
#     if(tmp.isdigit()): # tmp is digit number
#         print(pocketmon[int(tmp)])
#     else: # tmp is not number
#         print(pocketmon[tmp])

# # 10816 숫자 카드 2
# n = int(input())
# cardset = dict()
# cardinput = list(map(int, input().split()))
# for c in cardinput:
#     if c not in cardset:
#         cardset[c] = 0
#     cardset[c] += 1
# m = int(input())
# output = list(map(int, input().split()))
# for o in output:
#     if o not in cardset:
#         print(0, end=' ')
#     else:
#         print(cardset[o], end=' ')

# # 1764 듣보잡 . 말장난..
# n, m = map(int, input().split())
# hearset = set()
# seeset = set()
# for _ in range(n):
#     hearset.add(input())
# for _ in range(m):
#     seeset.add(input())
# intersect = sorted(hearset.intersection(seeset))
# print(len(intersect))
# print('\n'.join(intersect))

# # 1269 대칭 차집합
# a, b = map(int, input().split())
# setA = set(map(int, input().split()))
# setB = set(map(int, input().split()))
# print(len(setA ^ setB)) # 1 대칭차집합
# # print(len(setA.difference((setB)))+len(setB.difference(setA))) # 2 차집합

# # 10828 스택
# from collections import deque
# import sys
# class stack:
#     lst = deque([])
#     def push(self, x):
#         self.lst.append(x)
#     def pop(self):
#         if len(self.lst) == 0:
#             print(-1)
#         else:
#             print(self.lst.pop())
#     def size(self):
#         print(len(self.lst))
#     def empty(self):
#         if len(self.lst) == 0:
#             print(1)
#         else:
#             print(0)
#     def top(self):
#         if len(self.lst) == 0:
#             print(-1)
#         else:
#             print(self.lst[len(self.lst)-1])
#
# n = int(sys.stdin.readline())
# s = stack()
# while(n):
#     tmp = list(sys.stdin.readline().strip().split(' '))
#     if tmp[0] == "push":
#         s.push(tmp[1])
#     elif tmp[0] == "pop":
#         s.pop()
#     elif tmp[0] == "size":
#         s.size()
#     elif tmp[0] == "empty":
#         s.empty()
#     elif tmp[0] == "top":
#         s.top()
#     n -= 1

# # 10773 제로
# from collections import deque
# import sys
# class stack:
#     lst = deque([])
#     def push(self, x):
#         self.lst.append(x)
#     def pop(self):
#         self.lst.pop()
#     def sum(self):
#         sum = 0
#         for i in self.lst:
#             sum += i
#         print(sum)
#
# n = int(sys.stdin.readline())
# s = stack()
# while(n):
#     tmp = int(sys.stdin.readline())
#     if tmp == 0:
#         s.pop()
#     else:
#         s.push(tmp)
#     n -= 1
# s.sum()

# # 9012 괄호
# from collections import deque
# import sys
# class stack:
#     lst = deque([])
#     def push(self, x):
#         self.lst.append(x)
#     def pop(self):
#         self.lst.pop()
#     def top(self):
#         if len(self.lst) == 0:
#             return None
#         else:
#             return self.lst[len(self.lst)-1]
#     def empty(self):
#         if len(self.lst) == 0:
#             return True
#         else:
#             return False
#     def clear(self):
#         self.lst = deque([])
#
# n = int(sys.stdin.readline())
# s = stack()
# while(n):
#     tmp = sys.stdin.readline()
#     DC = True
#     for i in range(len(tmp)-1):
#         if tmp[i] == '(':
#             s.push('(')
#         elif tmp[i] == ')':
#             if s.top() == '(':
#                 s.pop()
#             else:
#                 DC = False
#                 break
#     if DC and s.empty(): print("YES")
#     else: print("NO")
#     s.clear()
#
#     n -= 1

# # 18258 큐 2
# import sys
# from collections import deque
#
# class queue:
#     q = deque([])
#     def push(self, x):
#         self.q.append(x)
#     def pop(self):
#         if len(self.q) == 0:
#             print(-1)
#         else:
#             print(self.q.popleft())
#     def size(self):
#         print(len(self.q))
#     def empty(self):
#         if len(self.q) == 0:
#             print(1)
#         else:
#             print(0)
#     def front(self):
#         if len(self.q) == 0:
#             print(-1)
#         else:
#             print(self.q[0])
#     def back(self):
#         if len(self.q) == 0:
#             print(-1)
#         else:
#             print(self.q[-1])
#
# n = int(sys.stdin.readline())
# q = queue()
# while(n):
#     cmd = deque(sys.stdin.readline().strip().split())
#     if cmd[0] == "push":
#         q.push(cmd[1])
#     elif cmd[0] == "pop":
#         q.pop()
#     elif cmd[0] == "size":
#         q.size()
#     elif cmd[0] == "empty":
#         q.empty()
#     elif cmd[0] == "front":
#         q.front()
#     elif cmd[0] == "back":
#         q.back()
#     n-=1

# # 2164 카드2
# # 데크를 사용해서 일단 정석적으로 풀어보기
# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# q = deque([i for i in range(1, n+1)])
# while(len(q) != 1):
#     # 맨 위 카드를 버린다
#     q.popleft()
#     # 맨 위 카드를 밑으로 옮긴다
#     q.append(q.popleft())
#
# # len이 1일 때 밖으로 빠져나온다
# print(q[0])

# # 10866 덱
# import sys
# class Deque:
#     dq = list([])
#     def push_front(self, x):
#         self.dq = [x] + self.dq
#     def push_back(self, x):
#         self.dq.append(x)
#     def pop_front(self):
#         if len(self.dq) == 0:
#             print(-1)
#         else:
#             print(self.dq.pop(0))
#     def pop_back(self):
#         if len(self.dq) == 0:
#             print(-1)
#         else:
#             print(self.dq.pop(-1))
#     def size(self):
#         print(len(self.dq))
#     def empty(self):
#         if len(self.dq) == 0:
#             print(1)
#         else:
#             print(0)
#     def front(self):
#         if len(self.dq) == 0:
#             print(-1)
#         else:
#             print(self.dq[0])
#     def back(self):
#         if len(self.dq) == 0:
#             print(-1)
#         else:
#             print(self.dq[-1])
# n = int(sys.stdin.readline())
# dq = Deque()
# while(n):
#     inp = sys.stdin.readline().strip().split()
#     if inp[0] == "push_front":
#         dq.push_front(int(inp[1]))
#     elif inp[0] == "push_back":
#         dq.push_back(int(inp[1]))
#     elif inp[0] == "pop_front":
#         dq.pop_front()
#     elif inp[0] == "pop_back":
#         dq.pop_back()
#     elif inp[0] == "size":
#         dq.size()
#     elif inp[0] == "empty":
#         dq.empty()
#     elif inp[0] == "front":
#         dq.front()
#     elif inp[0] == "back":
#         dq.back()
#
#     n-=1