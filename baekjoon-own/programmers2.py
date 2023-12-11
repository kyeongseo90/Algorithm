# # 택배 배달과 수거하기 https://school.programmers.co.kr/learn/courses/30/lessons/150369
# def solution(cap, n, deliveries, pickups):
#     answer = 0
#
#     truckDv = 0
#     truckPk = 0
#
#     # 뒤에서부터 탐색 -> 어차피 맨 뒤 n는 가야함
#     for i in range(n-1, -1, -1):
#         # 배달 수량 / 픽업 수량 이 둘 중 하나라도 0이 아니면
#         if deliveries[i] or pickups[i]:
#             cnt = 0
#             # i 번째 집에서 배송 / 픽업을 함
#             truckDv -= deliveries[i]
#             truckPk -= pickups[i]
#             # 음수일 경우 -> hub에 왔다가야함
#             while truckDv < 0 or truckPk < 0:
#                 truckDv += cap
#                 truckPk += cap
#                 cnt += 1
#             answer += (i+1) * 2 * cnt
#
#     return answer
#
# print("answer : 16, ", solution(4, 5, [1,0,3,1,2], [0,3,0,4,0]))
# print("answer : 30, ", solution(2, 7, [1,0,2,0,1,0,2], [0,2,0,1,0,2,0]))
import math


# # 미로 탈출 명령어 https://school.programmers.co.kr/learn/courses/30/lessons/150365
# # [n,m] 격자에서 0초:(x,y) -> k초:(r,c)
# # 1, 격자 바깥으로 나갈 수 없음
# # 2, 이동 거리가 총 k여야 함. 같은 격자 두번 이상 방문 가능
# # 3, 미로 탈출 경로 -> 문자열 사전순 가장 빠른 경로 -> BFS
# # l 왼, r 오, u 위, d 아래
# # 문자 사전순 : d -> l -> r -> u
# # 탈출 못하면 impossible 반환
#
# # DFS나 BFS로 풀면 스택이 터질 가능성이 높습니다
# # 사전 순이라는 조건에 유의하여 그리디로 풀어보세요
# # 도중에 장애물이 없으므로 거리는 맨해튼 거리로 계산됩니다
# # 출구까지의 거리가 4일 때, k=5라면 탈출할 수 있을까요? 아니면 k=6일 때는 어떠한지요?
# from collections import deque
# def solution(n, m, x, y, r, c, k):
#     impossible = "impossible"
#     answer = ""
#     dxy = [[1, 0, "d"], [0, -1, "l"], [0, 1, "r"], [-1, 0, "u"]]
#
#     manhattan = abs(x - r) + abs(y - c)
#     if (manhattan > k) or (k - manhattan) % 2 == 1:
#         return impossible
#
#     # dfs
#     flag = True
#     dq = deque()
#     dq.append((x, y, "", 0)) # x좌표, y좌표, 경로, 이동거리
#     while dq and flag:
#         x, y, route, dis = dq.pop()
#
#         for dx, dy, direct in reversed(dxy):
#             ax, ay, aroute = x + dx, y + dy, route + direct
#
#             # 격자 내에 존재하는지 유효성 검사
#             if 0 < ax <= n and 0 < ay <= m:
#                 # 이동거리, 도착 좌표 일치 검사 -> 일치하면 경로 리턴
#                 if dis == k and ax == r and ay == c:
#                     print(dis, route, direct)
#                     return aroute
#                 elif dis > k:
#                     flag = False
#                     break
#                 dq.append((ax, ay, aroute, dis+1))
#
#     return answer
#
# def solutionFailed(n, m, x, y, r, c, k):
#     answer = "impossible"
#     dxy = [[1, 0, "d"], [0, -1, "l"], [0, 1, "r"], [-1, 0, "u"]]
#     flag = True
#
#     manhatan = abs(x-r)+abs(y-c)
#     if (manhatan > k) or (k - manhatan) % 2 == 1:
#         return answer
#
#     dis = 0
#     dq = deque()
#     dq.append((x, y, ""))
#     while dq and flag:
#         cnt = len(dq)
#         dis += 1
#         for _ in range(cnt):
#             x, y, route = dq.popleft()
#             for dx, dy, direct in dxy:
#                 ax, ay, aroute = x + dx, y + dy, route + direct
#                 # 격자 내에 존재하는지 유효성 검사
#                 if 0 < ax <= n and 0 < ay <= m:
#                     # 이동거리, 도착 좌표 일치 검사 -> 일치하면 경로 리턴
#                     if dis == k and ax == r and ay == c:
#                         return route+direct
#                     elif dis > k:
#                         flag = False
#                         break
#                     dq.append((ax, ay, aroute))
#
#     return answer
#
#
# print(solution(3,4,2,3,3,1,5), ", answer = dllrl")
# print(solution(2,2,1,1,2,2,2), ", answer = dr")
# print(solution(3,3,1,2,3,3,4), ", answer = impossible")

# # 표현 가능한 이진트리
# import math
#
# def solution(numbers):
#     answer = []
#     for num in numbers:
#         answer.append(canPresentToBt(num))
#     return answer
#
#
# def canPresentToBt(num):
#     binary = str(bin(num))[2:]
#     print(binary, end=' ')
#     # 0 채워넣기
#     h = 0
#     while (int)(math.pow(2, h)) <= len(binary):
#         h += 1
#     if (int)(math.pow(2, h)-len(binary)) != 0:
#         tmp = '0' * (int)(math.pow(2, h) - len(binary))
#         binary = tmp + binary
#         print( (int)(math.pow(2, h) - len(binary)), end=' >> ')
#
#     print(h, binary)
#
#     if len(binary) % 2 != 0:
#         checkExceptLeaf(binary, len(binary) // 2, 0, len(binary)-1, 1)
#         return 1 if binary[len(binary) // 2] == '1' else 0
#     else:
#         half = len(binary) // 2
#         return 1 if binary[half] == '1' or binary[half + 1] == '1' else 0
#
#
# def checkExceptLeaf(binary, mid, start, end, flag):
#     if start >= end:
#         # leaf임
#         return binary[mid] or flag
#     elif binary[mid] == 0 and flag == 0:
#         return 0
#     elif binary[mid] == 0 and flag == 1:
#         flag = 0
#
#     # start ~ mid-1
#     haf1 = checkExceptLeaf(binary, (start + mid - 1) // 2, start, mid - 1, flag)
#     # mid+1 ~ end
#     haf2 = checkExceptLeaf(binary, (mid + 1 + end) // 2, mid + 1, end, flag)
#
#     return haf1 and haf2
#
# # print(str(bin(5)))
# print(solution([7,42,5]))
# print(solution([63, 111, 95]))
#
# # 이진수 앞에다가 포화이진트리가 될 때까지 0을 붙임
# # 어떤 노드가 0인데 그 자식이 1인 노드가 있다? 그러면 이진트리로 못만듬!!!


# # 2022 kakao tech internship : 코딩테스트 공부
# import math
# def solution(alp, cop, problems):
#     answer = 0
#     maxAlp, maxCop = alp, cop
#     for i, j, *a in problems:
#         maxAlp = max(maxAlp, i)
#         maxCop = max(maxCop, j)
#     print("maxAlp, maxCop : ", maxAlp, maxCop)
#
#     dp = [[math.inf] * (maxCop+1) for _ in range(maxAlp+1)]
#     dp[alp][cop] = 0
#
#     for i in range(alp, maxAlp+1):
#         for j in range(cop, maxCop+1):
#             # if i == 10 and j == 7:
#             #     print('잠깐 여기서 마지막으로 가는가?', dp[i][j])
#             if i != maxAlp:
#                 dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
#             if j != maxCop:
#                 dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
#             for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
#                 if i >= alp_req and j >= cop_req:
#                     alp_aft, cop_aft = min(i+alp_rwd, maxAlp), min(j+cop_rwd, maxCop)
#                     dp[alp_aft][cop_aft] = min(dp[alp_aft][cop_aft], dp[i][j] + cost)
#                     # if i == 10 and j == 7:
#                     #     print('어케됐누?', alp_aft, cop_aft, dp[alp_aft][cop_aft])
#             # # 코딩공부 1시간 혹은 알골공부 1시간
#             # dp[i][j] = min(dp[i][j], dp[i][j-1]+1, dp[i-1][j]+1)
#             # for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
#             #     dp[i][j] = min(dp[i][j], dp[i-cop_rwd][j-alp_rwd]+cost)
#
#     # for i in range(maxCop):
#     #     print(*dp[i])
#     for i in range(alp, maxAlp+1):
#         for j in range(cop, maxCop+1):
#             print(dp[i][j], end=' ')
#         print()
#     return dp[maxAlp][maxCop]
#
# # print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
# # print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
# print(solution(0,0,[[0,0,1,1,1],[150,150,1,1,100]]))
# print(solution(0,0,[[4,3,1,1,100],[0,0,2,2,1]]))
# print(solution(10, 1, [[1, 1, 1, 1, 1], [5, 5, 1, 1, 3]]))
# print(solution(0,0,[[0,0,30,2,1],[150,150,30,30,100]]))




# # 2022 KAKAO TECH INTERNSHIP > 두 큐 합 같게 만들기
# def solution(queue1, queue2):
#     answer = math.inf
#     queue = queue1 + queue2
#     if sum(queue) % 2 != 0:
#         return -1
#     half = sum(queue) // 2
#     start = 0
#     end = 0
#     rangeSum = queue[start]
#     cnt = 0
#     length = len(queue)
#     length1 = len(queue1)
#
#
#     while cnt < 3*length1:
#         if rangeSum == half:
#             # 이곳에서의 move 계산
#             move = 0
#             if end < length1 - 1:
#                 move = 3 * length1 + start + end + 1
#             else:
#                 move = start + (end - length1 + 1)
#             answer = min(answer, move)
#             print(move)
#         elif rangeSum < half:
#             end = (end+1)%length
#             rangeSum += queue[end]
#         else:
#             rangeSum -= queue[start]
#             start = (start+1)%length
#
#         cnt += 1
#
#
#     print(start, end, rangeSum, cnt)
#
#     if answer == math.inf:
#         return -1
#     return answer
#     # 결국 q1이 되느냐 q2가 되느냐의 문제인데 둘 다 계산해보고 더 적은 cnt가 필요한 거를 리턴하면 될듯-> ?못행
#     # half_idx = len(queue1)
#     # if (start < half_idx and end >= half_idx) \
#     #     or (end == half_idx):
#     #     std_s = 0
#     #     std_e = len(queue1) - 1
#     #     # answer
#     #     answer += start     # 앞에 있는거 빼기
#     #     answer +=       # 뒤에 있는거
#     # elif (start < half_idx and end < half_idx - 1) \
#     #     or (start >= half_idx and end < len(queue2)-1):
#     #     std_s = len(queue1)
#     #     std_e = len(queue) - 1
#     #     # answer
#     #     answer += start - std_e     # 앞에 있는거 빼기
#     #     answer +=
#     # else:
#
#
# print(solution([3, 2, 7, 2], [4, 6, 5, 1]), "answer =", 2)
# print(solution([1,2,1,2],[1,10,1,2]), "answer =", 7)
# print(solution([1,1],[1,5]), "answer =", -1)




# 2022 KAKAO TECH INTERNSHIP > 등산코스 정하기
# 산의 n개의 지점
# 각 지점은 출입구/쉼터/산봉우리
# 각 지점은 양방향 통행이 가능 -> 일정 시간 소요
# 등산 코스를 짜려고 함
# 출입구 한 곳에서 출발해서 -> 산봉우리 중 한 곳만 방문 -> 원래의 출입구로 돌아오는 코스
# 출입구 : 처음과 끝에 한 번씩만
# 산봉우리 : 한 번만 포함
# 등산 코스 안에 가장 길게 쉼 없이 이동해야하는 시간을 intensity라고 한다. 이것이 가장 짧은 등산코스를 찾아라
# n : 지점 수
# paths : 각 등산로의 정보 ([i, j, w] i와 j를 잇는 등산로는 w 시간이 걸린다.
# gates : 출입구들의 번호
# summits : 산봉우리들의 번호

# 출입구 -> ... -> 산봉우리 의 가장 intensity가 짧은 경로를 찾는다
import heapq
import math
def solution(n, paths, gates, summits):
    answer = []

    # 각 경로의 intensity
    intensity = [math.inf] * (n+1)

    # n번째가 summit(산봉우리)인지 판별
    isSummit = [False] * (n+1)
    for s in summits:
        isSummit[s] = True

    # 등산로
    route = [[] for _ in range(n+1)]
    for i, j, w in paths:
        # i,j에 산봉우리가 있으면 단일 경로만 저장
        if isSummit[i]:
            route[j].append((i, w))
        elif isSummit[j]:
            route[i].append((j, w))
        else:
            route[i].append((j, w))
            route[j].append((i, w))
    # 각 출입구를 0 지점과 단일연결. 시간도 0
    for g in gates:
        route[0].append((g, 0))

    # for i in route:
    #     print(i)

    intensity[0] = 0

    # djikstra 0부터 각 산봉우리까지
    heap = [] # (경로총비용 Cost, 현재 위치-지점 Location)
    heapq.heappush(heap, (0, 0))
    while heap:
        # print(heap, intensity)
        curC, curL = heapq.heappop(heap)
        for nxtL, nxtC in route[curL]:
            # 다음에 갈 경로가 내가 현재 가지고 있는 intensirt보다 더 작으면
            # 그 다음번 지점은 내가 가고있는 경로보다 더 intensirt가 더 작은 길이 확보되어 있다는 뜻이므로
            # heap에 넣지 않는다.
            # print(intensity[nxtL], intensity[curL], nxtC)
            if intensity[nxtL] <= max(intensity[curL], nxtC):
                continue
            intensity[nxtL] = max(intensity[curL], nxtC)
            heapq.heappush(heap, (intensity[nxtL], nxtL))

    # 산봉우리 intensity 중 가장 작은 산봉우리와 그의 intensity를 찾는다
    answer = [0, math.inf]
    summits.sort()
    # print(intensity)
    for s in summits:
        if intensity[s] < answer[1]:
            answer = [s, intensity[s]]
    return answer


print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],[5]), "answer [5,3]")
print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2, 4, 3]), "answer [3,4]")
print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[3, 7],[1, 5]), "answer [5,1]")
print(solution(5,[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],[1, 2],[5]), "answer [5,6]")