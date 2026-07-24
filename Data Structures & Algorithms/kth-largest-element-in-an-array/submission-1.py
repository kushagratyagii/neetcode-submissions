class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for i in nums:
            if len(minHeap)<k:
                heapq.heappush(minHeap,i)
            elif len(minHeap) == k and i>minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap,i)
        return minHeap[0]
        
        # maxHeap = [-i for i in nums]
        # heapq.heapify(maxHeap)

        # while k>1:
        #     heapq.heappop(maxHeap)
        #     k-=1
        # maxHeap.append(0)
        # return -maxHeap[0]



        

