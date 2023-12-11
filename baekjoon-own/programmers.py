# # 주어진 문자열을 가장 짧게 압축 시킬 수 있는 단위를 찾아 압축 결과의 길이를 출력하라.
# def solution(s):
#     iter = int(len(s) / 2)
#     lst = [len(s)] * 2
#     # check when 단위 = 2 ~ len(2)
#     for i in range(1, iter + 1):
#         comp = ""  # 압축된 문자열
#         j = i
#         n = 1   # iter number
#         stored = s[0:i]    # initial string
#         while(j <= len(s)):
#             tmp = s[j:j+i]
#             if stored == tmp:   # 반복 문자
#                 n += 1
#             else:               # 반복 문자가 아님. stored != tmp
#                 if n == 1:
#                     comp += stored
#                 else:
#                     comp += str(n) + stored
#                 stored = tmp
#                 n = 1
#             j += i
#         # 남는 경우
#         if len(tmp) < i:
#             comp += tmp
#         # 최종 글자 수
#         if i != 1:
#             lst.append(len(comp))
#         else:
#             lst[i] = len(comp)
#         print(i, comp)
#     return min(lst)
#
# print(solution("abcabcdede"))

# https://school.programmers.co.kr/learn/courses/30/lessons/60063
# 블록 이동하기
def solution(board):
    answer = 0
    robot = [[0, 0], [0, 1]]
    # bfs
    queue = []
    queue.append(robot)
    visit = set()
    visit.add(robot)
    while(True):

        for dd in cango(robot[0], robot[1], board)
    return answer

## 로봇이 움직이는 방향
# 1번이 시계 방향으로 움직임
# 1번이 반시계 방향으로 움직임
# 2번이 시계 방향으로 움직임
# 2번이 반시계 방향으로 움직임
#      # 1번의 움직임                2번의 움직임
# dx = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
# dy = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def cango(rob1, rob2, board):
    X, Y = 1, 0
    ret = []
    # X 좌표가 같음 => 세로
    if rob1[1] == rob2[1]:
        if rob1[0] > rob2[0]: rob1[0], rob2[0] = rob2[0], rob1[0] # swap
        # left side is empty
        if board[rob1[0]][rob1[1]-1] == board[rob2[0]][rob1[1]-1] == 0:
            ret.append([[rob1[0]+1, rob1[1]-1], rob2])
            ret.append([rob1, [rob2[0]-1, rob2[1]-1]])
        # right side is empty
        if board[rob1[0]][rob1[1] + 1] == board[rob2[0]][rob1[1] + 1] == 0:
            ret.append([[rob1[0] + 1, rob1[1]+1], rob2])
            ret.append([rob1, [rob2[0] - 1, rob2[1] + 1]])
    # Y 좌표가 같음 => 가로
    else:
        if rob1[1] > rob2[1]: rob1[1], rob2[1] = rob2[1], rob1[1] # swap
        # upside is empty
        if board[rob1[0]-1][rob1[1]] == board[rob2[0]-1][rob1[1]] == 0:
            ret.append([[rob1[0] - 1, rob1[1]+1], rob2])
            ret.append([rob1, [rob2[0] - 1, rob2[1] - 1]])
        # downside is empty
        if board[rob1[0]+1][rob1[1]] == board[rob2[0]+1][rob1[1]] == 0:
            ret.append([[rob1[0] + 1, rob1[1] + 1], rob2])
            ret.append([rob1, [rob2[0] - 1, rob2[1] + 1]])


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))

# n = int(input())
# house = list(map(int, input().split()))
# house.sort()
# print(house[int((n-1)/2)])