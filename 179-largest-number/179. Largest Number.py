class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n= len(nums)
        for i in range(n):
            nums[i]=str(nums[i])
        nums.sort(reverse=True, key=lambda i:(i*10))
        if(nums[0]=="0"):
            return "0"
        return "".join(nums)
        