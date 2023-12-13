import sys
strl = sys.stdin.readline()
q = int(sys.stdin.readline())
arr = [[0 for _ in range(26)] for _ in range(len(strl))]

arr[0][ord(strl[0])-97] = 1 # 첫글자 누적합
for i in range(1, len(strl)-1): # 2 ~ 끝 누적합
    for j in range(26):
        arr[i][j] = arr[i-1][j]
    arr[i][ord(strl[i])-97] += 1

for _ in range(q):
    a, b, c = list(sys.stdin.readline().split())
    b, c = int(b), int(c)
    if b == 0: # 0이면 c 부분 출력
        print(arr[c][ord(a) - 97])
    else: # 누적합이므로 c-(b-1) 출력
        print(arr[c][ord(a)-97] - arr[b-1][ord(a)-97])