# Topological Sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = {i : [] for i in range(numCourses)}
        res = []
        visit , cycle = set(),set()
        for crs,pre in prerequisites:
            adjacencyList[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit :
                return True
            cycle.add(crs)
            for i in adjacencyList[crs]:
                if dfs(i) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return[]
        return res