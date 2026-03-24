class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q=deque()
        time = 0
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while(q):
            if fresh==0:
                break
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in dirs:
                    nr,nc = r+dr,c+dc
                    if(0<=nr<m and 0<=nc<n and grid[nr][nc]==1):
                        fresh-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))
            time+=1
        return time if fresh==0 else -1
