class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            snum = str(num)
            for s in snum:
                ans.append(int(s))
        return ans
        