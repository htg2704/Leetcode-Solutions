class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        ans = []
        b = a[0]
        for i in a:
            if(b[1]>=i[0]):
                b[1] = max(b[1],i[1])
            else:
                ans.append(b)
                b = i
        ans.append(b)
        return ans   