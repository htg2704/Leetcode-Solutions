class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans, count = 1,1
        for i in range(len(prices)-1):
            if(prices[i]==prices[i+1]+1):
                count+=1
            else:
                count=1
            ans+=count
        return ans
        