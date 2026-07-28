class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        tray = []
        def backtrack():
            
            if len(tray) == len(nums):
                res.append(tray.copy())
                return
            for i in nums:
                if i not in tray:
                    tray.append(i)
                    backtrack()
                    tray.pop()

        backtrack()

        return res