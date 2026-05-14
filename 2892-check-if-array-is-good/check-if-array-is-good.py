class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)-1
        #print(n, nums.count(n))
        if(nums.count(n)!=2 or max(nums)>n):
            #print("b")
            return False
        s = set(nums)
        if(len(s)<n):
            return False
        for i in range(1,n-1):
            if i not in s:
                #print("blah")
                return False
        return True
        