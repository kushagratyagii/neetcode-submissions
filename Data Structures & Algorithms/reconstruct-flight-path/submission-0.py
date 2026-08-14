class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for source ,target in tickets:
            graph[source].append(target)

        for source in graph:
            graph[source].sort(reverse=True)
        res = []
        def dfs(source):
            while graph[source]:
                nextAirport = graph[source].pop()
                dfs(nextAirport)
            res.append(source)
        dfs("JFK")
        return res[::-1]

        