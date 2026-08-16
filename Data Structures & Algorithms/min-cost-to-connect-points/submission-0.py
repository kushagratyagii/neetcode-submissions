class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0,0)]
        seen = set()
        n = len(points)
        cost = 0

        while len(seen)<n:
            dist , i = heapq.heappop(minHeap)
            if i in seen:
                continue
            seen.add(i)
            cost += dist
            xi,yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj,yj = points[j]
                    dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(minHeap,(dist,j))
        return cost
