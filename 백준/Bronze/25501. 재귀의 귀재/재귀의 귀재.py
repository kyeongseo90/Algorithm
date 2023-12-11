def recursion(s, l, r, cnt):
  if l >= r: 
    return 1
  elif s[l] != s[r]: 
    return 0
  else:
    cnt[0] += 1
    return recursion(s, l+1, r-1, cnt)

def isPalindrome(s, cnt):
  cnt[0] += 1
  return recursion(s, 0, len(s)-1, cnt)

n = int(input())
while(n):
  n -= 1
  cnt = [0]
  str = input()
  res = isPalindrome(str, cnt)
  print(res, cnt[0])