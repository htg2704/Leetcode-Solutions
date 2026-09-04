class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxa, mina = [-1]*n, [10**10]*n
        maxa[0]=nums[0]
        mina[n-1]=nums[n-1]
        for i in range(1,n):
            maxa[i]=max(maxa[i-1], nums[i])
            mina[n-i-1]=min(mina[n-i], nums[n-i-1])
            
        for i in range(n):
            if(maxa[i]-mina[i]<=k):
                return i
        return -1
        

        