n = int(input())
A = list(map(int, input().split()))

NGE = [-1] * n
stack = []  # A의 인덱스 값이 저장됨

for i in range(n):
    # 스택에 A[i]을 넣다가 쌓여있는 값들보다 A[i]가 더 큰 것을 발견하면 아닐때까지 넣기
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

print(*NGE)