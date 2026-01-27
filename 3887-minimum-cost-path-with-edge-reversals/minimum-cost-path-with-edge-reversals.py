class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v,w))
            adj[v].append((u,2*w))
        dis = [inf]*n
        dis[0]=0
        heap=[(0,0)]
        while heap:
            d, u = heapq.heappop(heap)
            if u==n-1:
                return d
            if d!=dis[u]:
                continue
            for v, w in adj[u]:
                if dis[u]+w<dis[v]:
                    dis[v]=dis[u]+w
                    heapq.heappush(heap, (dis[v], v))
        return -1