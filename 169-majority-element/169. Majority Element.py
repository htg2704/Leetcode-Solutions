class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        e = 0
        for i in range(n):
            if(c==0):
                c+=1
                e=nums[i]
            elif(nums[i]==e):
                c+=1
            else:
                c-=1
        return e