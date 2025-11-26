class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod=10**9+7
        m,n = len(grid), len(grid[0])
        prev = [[0]*k for _ in range(n)]
        curr = [[0]*k for _ in range(n)]
        a = 0
        for i in range(n):
            a=(a+grid[0][i])%k
            prev[i][a]=1
        a=grid[0][0]%k
        for i in range(1,m):
            a=(a+grid[i][0])%k
            curr[0]=[0]*k
            curr[0][a]=1
            for j in range(1,n):
                curr[j]=[0]*k
                val = grid[i][j]
                for r in range(k):
                    nr = (r + val) % k
                    curr[j][nr] = (prev[j][r] + curr[j - 1][r]) % mod

            prev, curr = curr, prev

        return prev[n - 1][0] 