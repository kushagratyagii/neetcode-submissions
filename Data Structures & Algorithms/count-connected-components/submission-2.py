class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        ans = 0
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for j in adj[i]:
                
                dfs(j)
        for j in range(n):
            if j not in visit:
                dfs(j)
                ans+=1
        return ans