import sys

input = sys.stdin.readline
L, C = map(int, input().split())
## alpha = sorted(list(input().split()))
alpha = sorted(list(input().split()))

def pswd(tmp, i, cons, vowel):

    if i >= C:
        return

    aj = alpha[i]
    tmp += aj

    if aj == "a" or aj == "e" or aj == "i" or aj == "o" or aj == "u":
        vowel -= 1
    else:
        cons -= 1

    if len(tmp) == L :
        if cons <= 0 and vowel <= 0:
            print(tmp)
        return

    for j in range(i, C):
        pswd(tmp, j + 1, cons, vowel)


for i in range(C-L+1):
    pswd("", i, 2, 1)
