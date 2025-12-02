class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d = defaultdict(int)
        for p in points:
            d[p[1]]+=1
        Sum, count2 = 0,0
        for f in d.values():
            if f<=1:
                continue
            count=f*(f-1)//2
            Sum+=count
            count2+=count**2
        return (Sum**2-count2)//2%(10**9+7)


        