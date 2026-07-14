class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        maxl=0
        cursum = 0
        l, r = 0,0
        target = s - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        while(r<len(nums)):
            cursum +=nums[r]
            while(l<=r and cursum>s-x):
                cursum-=nums[l]
                l+=1
            if (cursum==s-x):
                maxl=max(maxl, r-l+1)
            r+=1
        if maxl==0:
            return -1
        return len(nums)-maxl