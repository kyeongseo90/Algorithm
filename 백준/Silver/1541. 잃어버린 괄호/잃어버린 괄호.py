fm = input()
nums = list(map(int, fm.replace('+', '-').split('-')))
minus, x = 1, 1
result = nums[0]
for i in fm:
    if i == '+':
        result += nums[x] * minus
        x += 1
    elif i == '-':
        minus = -1
        result -= nums[x]
        x += 1
print(result)