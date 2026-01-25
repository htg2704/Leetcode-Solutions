class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [0]*len(nums)
        pref[0]=nums[0]
        for i in range(1,len(nums)):
            pref[i]=pref[i-1]+nums[i]
        if(pref[-1]-pref[0]==0):
            return 0
        for i in range(1,len(pref)):
            if(pref[i-1]==(pref[-1]-pref[i])):
                return i
        return -1
        