class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxs, curs=0,0
        l, r = 0, len(nums)-1
        while(r>=l):
            curs=nums[l]+nums[r]
            maxs=max(maxs, curs)
            r-=1
            l+=1
        return maxs
        