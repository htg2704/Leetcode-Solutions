class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        s = set(range(1,n+1))
        for i in range(1,n):
            for j in range(i+1,n+1):
                c2=(i*i)+(j*j)
                if sqrt(c2) in s:
                    ans+=2
        return ans
        