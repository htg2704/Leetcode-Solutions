class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = len(s)
        a, b  =0,0
        for c in s:
            a+=(c=='a')
        for c in s:
            a-=(c=='a')
            ans=min(ans, a+b)
            b+=(c=='b')
        return ans