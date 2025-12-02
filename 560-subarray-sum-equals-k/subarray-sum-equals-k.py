class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = {}
        s, ans = 0,0
        d[0]=1
        for i in range(n):
            s+=nums[i]
            rem = s-k
            if rem in d:
                ans+=d[rem]
            if s not in d:
                d[s]=1
            else:
                d[s]+=1
        return ans