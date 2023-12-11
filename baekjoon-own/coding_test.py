## SK 1
def solution(money, costs):
    answer = 0
    won = [1, 5, 10, 50, 100, 500]
    i=0
    for j in costs:
        for c in range(i+1, len(costs)):
            dup = costs[i] * (won[c] / won[i])
            if dup < costs[c]:
                costs[c] = dup
        i+=1

    i = 5
    for c in reversed(costs):
        ahr, money = divmod(money, won[i])
        answer += c * ahr;
        i-=1
    return answer

arr = [1, 4, 99, 35, 50, 1000]
print(solution(4578, arr))


## SK 2
def solution(n, clockwise):
    answer = [[0 for i in range(n)] for j in range(n)]
    x, y = 0, 0

    rot = (1, 1, -1, -1)

    adv = n-1

    for start in range(4):
        cnt = 1
        if start == 0:
            x = 0
            y = 0
        elif start == 1:
            x = 0
            y = n-1
        elif start == 2:
            x = n-1
            y = n-1
        else:
            x = n-1
            y = n-1

        for ai in reversed(range(1, adv)):
            while(ai > 0):
                answer[x][y] = cnt
                ai -= 1
                cnt += 1

                if clockwise == True:
                    if(start % 2 == 1): # odd
                        x = x + rot[start]
                    else: # even
                        y = y + rot[start]
                else: # clockwise == False
                    if (start % 2 == 1):  # odd
                        y = y + rot[start]
                    else:  # even
                        x = x + rot[start]

            start = (start + 1) % 4
            print(answer)
    return answer

print(solution(5, True))



## SK 3
def solution(width, height, diagonals):
    answer = 0
    w_max = 0
    h_max = 0
    for x, y in diagonals:
        w_max = max(w_max, x, width-x+1)
        h_max = max(h_max, y, height-y+1)

    arr = [[0 for i in range(h_max+1)] for j in range(w_max+1)]
    for x in range(w_max + 1):
        for y in range(h_max + 1):
            if x==0 and y==0:
                arr[x][y] = 0
            elif x == 0:
                arr[x][y] = 1
            elif y == 0:
                arr[x][y] = 1
            else:
                arr[x][y] = arr[x-1][y]+arr[x][y-1]

    for x, y in diagonals:
        x1, y1 = x, y-1
        x2, y2 = x-1, y
        # (0,0 ~ x,y) * (x,y ~ width,height)
        answer += arr[x1][y1] * arr[width - x2][height - y2]
        answer += arr[x2][y2] * arr[width - x1][height - y1]
        answer %= 10000019
    return answer

width = 51
height = 37
diagonals=[[17,19]]
print(solution(width, height, diagonals))



## SK 4
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print(self):
        print(self.data)

def distance(i,j,k,n):
    for i in range(n):


def solution(n, edges):
    answer = 0

    for i in range(n):
        for j in range(n):
            if i==j: break
            for k in range(n):
                if i==k or j==k: break
                if distance(i,j,k, n)
                    answer+=1

    return answer
