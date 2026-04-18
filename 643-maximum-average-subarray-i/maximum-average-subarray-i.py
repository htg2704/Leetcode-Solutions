class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxs, s = 0,0
        for i in range(k):
            s+=nums[i]
        maxs=s
        for i in range(k, len(nums)):
            s+=(nums[i]-nums[i-k])
            maxs = max(maxs, s)
        return maxs/k
        