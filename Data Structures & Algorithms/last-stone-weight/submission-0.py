class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1*i for i in stones]
        heapq.heapify(maxHeap)

        while(len(maxHeap)>1):
            first,second = -1*heapq.heappop(maxHeap),-1*heapq.heappop(maxHeap)
            if first>second:
                heapq.heappush(maxHeap,second-first)

        maxHeap.append(0)
        return abs(maxHeap[0])