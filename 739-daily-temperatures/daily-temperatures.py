class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0]*n
        a = []
        for i in range(n):
            while a and temp[i]>a[-1][0]:
                T, I = a.pop()
                ans[I] = i - I
            a.append((temp[i], i))
        return ans