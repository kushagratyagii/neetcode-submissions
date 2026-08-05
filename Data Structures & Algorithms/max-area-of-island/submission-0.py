class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_a = 0
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=1:
                return 0
            else:
                grid[i][j] = 0
                max_a = 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            return max_a
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_a = max(max_a,dfs(i,j))
        return max_a