class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        s = ""
        for i in range(len(nums)):
            s+=str(nums[i])
            bin = int(s,2)
            if(bin%5==0):
                ans.append(True)
            else:
                ans.append(False)
        return ans
        