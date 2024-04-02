class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        a = []
        for i in range(len(nums)):
            if(target-nums[i] in s):
                a.append(i)
                a.append(nums.index(target-nums[i]))
                return a;
            s.add(nums[i])
            