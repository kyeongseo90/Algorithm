import sys
input = sys.stdin.readline

n, m = map(int, input().split())
passwords = {}

for i in range(n):
    site, pswd = input().split()
    passwords[site] = pswd

for i in range(m):
    site = input().strip()
    print(passwords.get(site))