class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0]*n
        a = []
        for i in range(n):
            while a and temp[i]>temp[a[-1]]:
                id = a.pop()
                ans[id] = i - id
            a.append(i)
        return ans