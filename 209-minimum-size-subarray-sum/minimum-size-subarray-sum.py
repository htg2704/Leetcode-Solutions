class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0,0
        cur = 0
        ans= inf
        for r in range(len(nums)):
            cur+=nums[r]
            while(cur>=target):
                if(r-l+1<ans):
                    ans=r-l+1
                cur-=nums[l]
                l+=1
        return ans if ans is not inf else 0
            


        