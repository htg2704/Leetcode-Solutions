class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(board, row, col):
            r, c = row, col
            while r>=0 and c>=0:
                if(board[r][c]=='Q'):
                    return False
                r-=1
                c-=1
            r, c = row, col
            while r>=0:
                if(board[r][c]=='Q'):
                    return False
                r-=1
            r, c = row, col
            while r>=0 and c<n:
                if(board[r][c]=='Q'):
                    return False
                r-=1
                c+=1
            return True

        def fun(row, ans, board):
            if(row==len(board)):
                ans.append(["".join(r) for r in board])
                return
            for col in range(n):
                if isSafe(board, row, col):
                    board[row][col]='Q'
                    fun(row+1, ans, board)
                    board[row][col]='.'

        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        fun(0, ans, board)
        return ans