class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        max_l = height[l]
        max_r = height[r]
        res = 0
        while(l<r):
            potential_store = min(max_l,max_r)

            if max_l > max_r:
                r -= 1
                max_r = max(max_r,height[r])
                res += max_r - height[r]

            else:
                l += 1
                max_l = max(max_l,height[l])
                res += max_l - height[l]

        return res