class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS ,COLS = len(grid),len(grid[0])
        time = 0
        visit = set()
        n_fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    n_fresh+=1
        
        while q and n_fresh >0:
            for i in range(len(q)):
                r,c = q.popleft()
                nei = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in nei:
                    row = r+dr
                    col = c+dc
                    if (row < 0 or row >= ROWS or col < 0 or col >= COLS):
                        continue
                    if grid[row][col] == 1 :
                        n_fresh -= 1
                        grid[row][col] = 2
                        visit.add((row,col))
                        q.append((row,col))
            time+=1
        return time if n_fresh == 0 else -1