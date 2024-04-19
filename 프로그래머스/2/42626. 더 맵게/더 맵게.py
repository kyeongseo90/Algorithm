import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while (True):
        minValue = heapq.heappop(scoville)
        if minValue >= K:
            return answer
        if len(scoville) == 0 and minValue < K:
            return -1
        secMin = heapq.heappop(scoville)
        heapq.heappush(scoville, minValue+2*secMin)
        answer += 1
    return answer