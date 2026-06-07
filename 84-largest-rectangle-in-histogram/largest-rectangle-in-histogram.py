class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxa = 0
        a = []
        n =len(heights)
        for i in range(n):
            start = i
            while a and a[-1][1]>heights[i]:
                ind, h = a.pop()
                maxa = max(maxa, h*(i-ind))
                start = ind
            a.append((start,heights[i]))
        
        for i, h in a:
            maxa=max(maxa, h*(n-i))
        return maxa