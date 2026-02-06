class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        rem = 0
        for j in range(len(nums)):
            while nums[j] > nums[i] * k:
                i += 1
            rem = max(rem, j - i + 1)
            
        return len(nums) - rem
        