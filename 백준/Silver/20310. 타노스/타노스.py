str = input()
cnt0 = str.count('0') / 2
cnt1 = str.count('1') / 2

ans = ''
for c in str:
    if (c == '0' and cnt0 != 0):
        ans += c
        cnt0 -= 1
    elif (c == '1' and cnt1 == 0):
        ans += c
    elif (c == '1'):
        cnt1 -= 1

print(ans)