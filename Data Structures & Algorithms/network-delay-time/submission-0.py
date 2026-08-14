class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjDict = collections.defaultdict(list)
        for u,v,w in times:
            adjDict[u].append((w,v))

        visit = set()
        minHeap = [(0,k)]
        t = 0

        while minHeap:
            edge,vertex = heapq.heappop(minHeap)

            if vertex in visit:
                continue
            t = max(t,edge)
            visit.add(vertex)
            for cost,neighbour in adjDict[vertex]:
                if neighbour not in visit:
                    
                    heapq.heappush(minHeap,(edge+cost,neighbour))

        return t if len(visit) == n else -1