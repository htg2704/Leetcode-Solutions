class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s=set()
        maxs = 0
        cur=0
        start = 0
        for end in range(len(nums)):
            while(nums[end] in s or len(s)==k):
                s.remove(nums[start])
                cur-=nums[start]
                start+=1
            cur+=nums[end]
            s.add(nums[end])
            if(len(s)==k):
                maxs=max(maxs, cur)
        return maxs



        