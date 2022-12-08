def solution(n):
    dp = {}
    dp[1] = 1
    dp[2] = 2
    if n <= 2:
        return dp[n]
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n] % 1234567
