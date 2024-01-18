import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
materials = list(map(int, input().split()))

materials.sort()

st, end = 0, N-1
result = 0
while(st < end):
    mat = materials[st] + materials[end]
    if M == mat:
        result += 1
        st, end = st+1, end-1
    elif M > mat:
        st+=1
    else:
        end -= 1

print(result)