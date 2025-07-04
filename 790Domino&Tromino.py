class Solution(object):
    def numTilings(self, n):
        MOD = 10**9 + 7
        if n <= 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 5
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3])  % MOD
        return dp[n]
        
sol = Solution()
n_values = [1, 2, 3, 4, 5]
for n in n_values:
    print(sol.numTilings(n))
    