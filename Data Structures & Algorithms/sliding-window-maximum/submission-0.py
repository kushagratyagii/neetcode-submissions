import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        output = []
        l = 0
        r = 0

        while(r<len(nums)):
            while deque and (nums[deque[-1]]<nums[r]):
                deque.pop()
            deque.append(r)

            if(l>deque[0]):
                deque.popleft()


            #this is the edge case of it
            if(r+1) >= k:
                output.append(nums[deque[0]])
                l+=1

            r += 1
        return output