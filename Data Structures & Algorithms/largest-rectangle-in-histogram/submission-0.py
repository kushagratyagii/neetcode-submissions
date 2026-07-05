class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        n = len(heights)
        for ind,val in enumerate(heights):
            start = ind
            while(stack and stack[-1][1]>val):
                a,b = stack.pop()
                w = ind - a
                res = max(res,w*b)
                start = a
            stack.append([start,val])
        while stack:
            a,b = stack.pop()
            w = n - a
            res= max(res , w * b)
        return res