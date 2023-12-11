# # 11401 이항 계수
# NUM = 1000000007
#
# N, K = map(int, input().split())
#
# def binomial_coe(n, k):
#     if k == 0 or n == 1 or n == k:
#         return 1
#
#     return binomial_coe(n-1, k-1) + binomial_coe(n-1, k)
#
# print(binomial_coe(N, K) % NUM)

# # 2042 구간 합 구하기
# # 세그먼트 트리를 이용하면 구간합을 구하거나 수정할 때 O(logN)의 시간으로 처리가능
# import sys
#
# def makeST(idx, left, right):
#     if left > right:
#         return
#     elif left == right:
#         segtree[idx] = nums[right] - nums[right-1]
#         return
#     segtree[idx] = nums[right] - nums[left-1]
#     makeST(idx*2, left, (left+right)//2)
#     makeST(idx*2+1, (left+right)//2+1, right)
#
# # start, end : node에 해당하는 인덱스 구간
# # node : array 내 현재 위치
# # l, r : 구하고자 하는 인덱스 구간
# def sum(start, end, node, l, r):
#     if l > end or r < start:    # 범위 밖에 있는 경우
#         return 0
#     if l <= start and end <= r: # 범위 안에 있는 경우
#         return segtree[node]
#
#     # 둘 다 아닌 경우
#     # 두 구간으로 나누어 다시 구하기 (자식 노드로 가기)
#     return sum(start, (start+end) // 2, node*2, l, r) \
#         + sum((start+end) // 2 + 1, end, node*2 + 1, l, r)
#
# # start, end : node에 해당하는 인덱스 구간
# # node : array 내 현재 위치
# # idx : 구간 합 수정해야 할 노드
# # diff : 해당 노드가 포함된 구간일 때 수정 값
# def update(start, end, node, idx, diff):
#     # 변경할 idx 값이 범위 바깥이면 확인 불필요
#     if idx < start or end < idx:
#         return
#
#     # 범위 안쪽인 경우
#     segtree[node] += diff   # 차이 저장
#     # 리프노드가 아니면 아래 자식들도 확인
#     if start != end :
#         update(start, (start+end)//2, node*2, idx, diff)
#         update((start+end)//2+1, end, node*2+1, idx, diff)
#
#
# N, M, K = map(int, sys.stdin.readline().strip().split())
# num = [0]
# nums = [0] # 누적합 저장 배열
# for i in range(N):
#     tmp = int(sys.stdin.readline().strip())
#     num.append(tmp)
#     nums.append(tmp + nums[i])
#
# # make segment tree
# segtree = [0] * (N*4)
# makeST(1, 1, N)
#
# # sum or update
# for i in range(M+K):
#     a, b, c = map(int, sys.stdin.readline().strip().split())
#     if a == 1:
#         diff = c - num[b]
#         num[b] = c
#         update(1, N, 1, b, diff)
#     else:
#         print(sum(1, N, 1, b, c))
