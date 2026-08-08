class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board),len(board[0])
        def connected(r,c):
            if r<0 or r>= ROWS or c<0 or c>=COLS or board[r][c]!='O':
                return
            board[r][c] = 'T'
            connected(r+1,c)
            connected(r-1,c)
            connected(r,c+1)
            connected(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0,ROWS-1] or c in [0,COLS-1]) and board[r][c]=='O':
                    connected(r,c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        
