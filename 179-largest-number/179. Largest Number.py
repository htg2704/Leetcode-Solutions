class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        nums.sort(reverse=True, key=lambda i:(i*10))
        if(nums[0]=="0"):
            return "0"
        return "".join(nums)
        