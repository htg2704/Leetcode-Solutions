class Solution:
    import math
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mini=[inf]*(k-1)+[0]
        pref, ans = 0, -inf
        for i in range(n):
            pref+=nums[i]
            ik=i%k
            ans=max(ans, pref-mini[ik])
            mini[ik]=min(pref, mini[ik])
        return ans
        