class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i,tray,sum):
            
            if sum == target:
                res.append(tray.copy())
                return
            if sum > target or i >= len(nums):
                return
            tray.append(nums[i])
            dfs(i,tray,sum+nums[i])
            tray.pop()
            dfs(i+1,tray,sum)

        dfs(0,[],0)
        return res

