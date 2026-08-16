class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0],0,0)]
        visit = set()
        visit.add((0,0))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while minHeap:
            height,r,c = heapq.heappop(minHeap)
            
            if r==N-1 and c==N-1:
                return height
            for dr,dc in directions:
                row,col = r+dr,c+dc

                if (row<0 or row>=N or col<0 or col>=N or (row,col) in visit):
                    continue
                heapq.heappush(minHeap,(max(height,grid[row][col]),row,col))
                visit.add((row,col))