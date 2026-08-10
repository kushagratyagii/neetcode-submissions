class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        rank = [0] * (N+1)
        par = [i for i in range(N+1)]

        def findpar(n):
            if n != par[n]:
                par[n] = findpar(par[n])
            return par[n]
        def union(n1,n2):
            p1,p2 = findpar(n1),findpar(n2)
            if p1 == p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        