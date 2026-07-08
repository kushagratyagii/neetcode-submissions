class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1

        while(l<r):
            m = (l+r)//2

            
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        min_i = r
        
        if target >= nums[0] and target <= nums[min_i-1]:
            l,r = 0,min_i-1
            
        if target >= nums[min_i] and target <= nums[n-1]:
            l,r = min_i,n-1
            
        if nums[min_i]  ==  nums[0]:
            l,r = 0,n-1
            
        
        
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1
            