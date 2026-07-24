class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-i for i in nums]
        heapq.heapify(maxHeap)

        while k>1:
            heapq.heappop(maxHeap)
            k-=1
        maxHeap.append(0)
        return -maxHeap[0]



        

