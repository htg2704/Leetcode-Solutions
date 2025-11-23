class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n, neg = len(nums), -(1<<30)
        dp=[[0,0,0],[0,neg, neg]]
        for i in range(len(nums)):
            x = nums[i]%3
            for mod in range(3):
                prevmod=(3+mod-x)%3
                take=nums[i]+dp[(i+1)&1][prevmod]
                skip=dp[(i+1)&1][mod]
                dp[i&1][mod]=max(take, skip)
        return max(0,dp[(n-1)&1][0])
