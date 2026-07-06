class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m*n
        l,r = 0,t-1

        while(l<=r):
            m = (l+r)//2
            row = m//n
            col = m%n

            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = m-1
            if matrix[row][col] < target:
                l = m+1

        return False