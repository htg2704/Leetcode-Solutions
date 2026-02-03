class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        flag = 1
        if(nums[1]<nums[0]):
            return False
        for i in range(len(nums)-1):
            if((flag==1 and nums[i]<nums[i+1]) or (flag==2 and nums[i]>nums[i+1]) or (flag==3 and nums[i]<nums[i+1])):
                continue
            if(flag==1 and nums[i]>nums[i+1]):
                flag+=1
            elif(flag==2 and nums[i]<nums[i+1]):
                flag+=1
            elif(flag==3 and nums[i]>nums[i+1]):
                return False
            else:
                return False
        return flag==3
        
            

        