class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right and self.right[0]<num:
            heapq.heappush(self.right,num)
        else:
            heapq.heappush(self.left, -1 * num)
        if len(self.left) > len(self.right)+1:
            val = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right,val)
        elif len(self.right)>len(self.left)+1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left,-1 * val)

    def findMedian(self) -> float:
        if (len(self.left)+len(self.right))%2 == 0:
            return (-1*self.left[0]+self.right[0])/2.0
        else:
            return -1*self.left[0] if len(self.left)>len(self.right) else self.right[0]
        