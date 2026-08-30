class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxe, mine, mini, maxi = -10**6, 10**6, 0,0
        for i in range(len(nums)):
            if(nums[i]>maxe):
                maxe=nums[i]
                maxi = i
            if(nums[i]<mine):
                mine=nums[i]
                mini = i
        n = len(nums)
        l = min(mini, maxi)
        r = max(mini, maxi)
        n = len(nums)
        return min(r + 1, n - l,l + 1 + n - r  )
    