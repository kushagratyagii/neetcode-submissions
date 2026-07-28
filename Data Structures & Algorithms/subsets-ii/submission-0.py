class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tray = []
        res = []

        def backtrack(i,tray):
            if i>=len(nums):
                res.append(tray.copy()) 
                return
            tray.append(nums[i])
            backtrack(i+1,tray)
            tray.pop()
            
            while i+1<len(nums) and nums[i] == nums[i+1] :
                i+=1
            backtrack(i+1,tray)
            
        backtrack(0,[])
        return res