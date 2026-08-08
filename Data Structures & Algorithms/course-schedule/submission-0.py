class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacencyList = defaultdict(list)
        adjacencyList = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adjacencyList[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if adjacencyList[crs] == []:
                return True
            visiting.add(crs)
            for pre in adjacencyList[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            adjacencyList[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
