from collections import deque
class Solution:
    def bfs(self,sr,sc, image, newColor, cur):
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        m,n = len(image),len(image[0])
        q = deque()
        q.append((sr,sc))
        image[sr][sc]=newColor
        while(q):
            sr,sc = q.popleft()
            for dr,dc in dirs:
                nr,nc = sr+dr,sc+dc
                if(nr>=0 and nr<m and nc>=0 and nc<n and image[nr][nc]==cur):
                    image[nr][nc]=newColor
                    q.append((nr,nc))
    def floodFill(self, image, sr, sc, newColor):
        cur = image[sr][sc]
        if image[sr][sc] == newColor:
            return image
        self.bfs(sr,sc, image, newColor, cur)
        return image

      