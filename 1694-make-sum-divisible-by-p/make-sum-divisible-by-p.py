class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        target = s%p
        if target==0:
            return 0
        map = {0:-1}
        pref = 0
        ans=len(nums)
        for i in range(len(nums)):
            pref=(pref+nums[i])%p
            need = (pref-target+p)%p
            if need in map:
                ans=min(ans, i-map[need])
            map[pref]=i
        if ans==len(nums):
            return -1
        return ans