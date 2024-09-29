class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans,m = -100000,0
        for i in range(len(nums)):
            m = m+nums[i]
            if(ans<m):
                ans = m
            if(m<0):
                m=0
        return ans
        