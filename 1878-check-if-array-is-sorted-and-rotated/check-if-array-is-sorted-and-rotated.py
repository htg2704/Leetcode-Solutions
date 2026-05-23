class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                count+=1
        if count==1 and nums[0]<nums[-1]:
            return False
        return False if count>1 else True
        