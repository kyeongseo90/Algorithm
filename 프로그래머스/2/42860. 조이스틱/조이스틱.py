def solution(name):
    
    # print('A', ord('A'), 'Z', ord('Z')) # A = 65, Z = 90
    
    length = len(name)
    
    alpha_total = 0
    # 최대 좌우 움직이는 경우: 마지막까지 쭉 한방향으로 가는 거
    move_min = length - 1
    
    # 각 위치에서 조이스틱을 위아래 중 어디로 움직여야 최소로 움직이는지 계산 & 모든 횟수를 더함
    for i in range(length):
        c = name[i]
        
        alpha_total += min(ord(c)-65, 91-ord(c))
        
        # 해당 부분을 꺾이는 부분으로 본다면, 다음부분 A가 몇개 연속으로 있는지 확인
        tmp = i + 1
        while (tmp < length and name[tmp] == 'A'):
            tmp += 1
        
        # 기존 vs 오른쪽으로 갔다가 왼쪽으로 tmp까지 쭉 vs 왼쪽으로 tmp까지 갔다가 오른쪽 i까지 쭉
        move_min = min(move_min, 2 * i + (length-tmp), 2 * (length-tmp) + i)
        # print(i, tmp, move_min)
        
    
    return alpha_total + move_min
            
