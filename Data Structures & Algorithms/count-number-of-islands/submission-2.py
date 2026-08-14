class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        res = 0

        def bfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visit or grid[r][c] !="1":
                return
            visit.add((r,c))
            grid[r][c] = "0"
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c]=="1":
                    res += 1
                    bfs(r,c)
        return res