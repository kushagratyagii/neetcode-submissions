class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,tray,sum):
            
            if sum == target:
                res.append(tray.copy())
                return
            if sum > target or i >= len(nums):
                return
            tray.append(nums[i])
            dfs(i+1,tray,sum+nums[i])
            tray.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1,tray,sum)

        dfs(0,[],0)
        return res

