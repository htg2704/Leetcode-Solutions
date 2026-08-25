class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        m = max(nums)
        x = k
        while(m>=k):
            if k not in s:
                return k
            k+=x
        return k
        