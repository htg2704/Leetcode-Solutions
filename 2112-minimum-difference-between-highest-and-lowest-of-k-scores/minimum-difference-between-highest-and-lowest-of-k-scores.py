class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mins = inf
        if(k==1):
            return 0
        for i in range(len(nums)-k+1):
            #print(i,nums[i+k-1],nums[i])
            mins=min(mins, nums[i+k-1]-nums[i])
            #print(mins)
        return mins

        