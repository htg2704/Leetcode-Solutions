class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        n=len(nums)
        ans = [1]*n
        for i in range(n):
            ans[i]=a
            a=a*nums[i]
        a=1
        for i in range(n-1,-1,-1):
            ans[i]*=a
            a=a*nums[i]
        return ans

        
        