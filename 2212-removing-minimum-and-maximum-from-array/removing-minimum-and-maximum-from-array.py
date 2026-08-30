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
        mid = n//2
        if(mini<=mid and maxi<=mid):
            return max(mini, maxi)+1
        elif(mini>=mid and maxi>=mid):
            return n-min(mini, maxi)
        else:
            l = min(mini, maxi)
            r = max(mini, maxi)
            return min(l+1+(n-r), n-l, r+1)
        
        
        
        