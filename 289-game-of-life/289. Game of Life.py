class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        m = len(board[0])
        n = len(board)

        for i in range(n):
            for j in range(m):
                c=0
                for dx, dy in dir:
                    x = i+dx
                    y=j+dy
                    if((0<=x<n) and (0<=y<m) and (board[x][y]==1 or board[x][y]==2)):
                        c+=1
                if(board[i][j]==1):
                    if c<2 or c>3:
                        board[i][j]=2
                else:
                    if c==3:
                        board[i][j]=-1
        
        for i in range(n):
            for j in range(m):
                if(board[i][j]==-1):
                    board[i][j]=1
                elif(board[i][j]==2):
                    board[i][j]=0
        """
        Do not return anything, modify board in-place instead.
        """
        