class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9+7
        ans = 0
        dp = [0]*26
        for ch in s:
            i = ord(ch)-97
            x = ans-dp[i]+1
            ans = (ans+x)%mod
            dp[i]=(dp[i]+x)%mod
        return ans

        