import math
def solution(alp, cop, problems):
    answer = 0
    maxAlp, maxCop = alp, cop
    for i, j, *a in problems:
        maxAlp = max(maxAlp, i)
        maxCop = max(maxCop, j)

    dp = [[math.inf] * (maxCop+1) for _ in range(maxAlp+1)]
    dp[alp][cop] = 0

    for i in range(alp, maxAlp+1):
        for j in range(cop, maxCop+1):
            if i != maxAlp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j != maxCop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    alp_aft, cop_aft = min(i+alp_rwd, maxAlp), min(j+cop_rwd, maxCop)
                    dp[alp_aft][cop_aft] = min(dp[alp_aft][cop_aft], dp[i][j] + cost)
                    
    return dp[maxAlp][maxCop]