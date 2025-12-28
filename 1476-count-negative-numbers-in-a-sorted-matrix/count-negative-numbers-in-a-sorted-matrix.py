class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n-1,-1, -1):
                if(grid[i][j]>=0):
                    ans+=(n-j-1)
                    break
            else:
                ans+=n
        return ans


        