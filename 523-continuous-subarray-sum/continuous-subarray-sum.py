class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}
        s = 0
        d[0]=-1
        for i in range(len(nums)):
            s+=nums[i]
            rem=s%k
            if(rem in d):
                if(i-d[rem]>1):
                    return True
            else:
                d[rem]=i
        return False
        