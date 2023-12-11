# 6549 히스토그램에서 가장 큰 직사각형
import sys
while(True):
    lst = list(map(int, sys.stdin.readline().strip().split()))
    if lst[0] == 0:
        break

    # index 1부터 index lst[0]번째까지
