from collections import defaultdict
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        
        stack = [] # pairs of value,index

        for i,t in enumerate(temperatures):
            while (stack and (stack[-1][1]<t)):
                ind,val = stack.pop()
                res[ind] = i- ind
            stack.append([i,t])
            
        return res

