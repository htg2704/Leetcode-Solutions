class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def fun(n, last, k, nums, ans):
            if n==0 and k==len(nums):
                ans.append(list(nums))
                return
            if n<=0 or k<len(nums):
                return
            for i in range(last, 10):
                if i<=n:
                    nums.append(i)
                    fun(n-i, i+1, k, nums, ans)
                    nums.pop()
                else:
                    break

        ans, nums = [],[]
        fun(n, 1, k, nums, ans)
        return ans 
        