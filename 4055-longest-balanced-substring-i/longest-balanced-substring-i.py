class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            c = defaultdict(int)
            for j in range(i,n):
                c[s[j]]+=1
                if len(set(c.values()))==1:
                    ans=max(ans, j-i+1)
        return ans
        