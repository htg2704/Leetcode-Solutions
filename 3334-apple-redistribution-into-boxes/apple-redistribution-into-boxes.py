class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        total, ans = 0,0
        while total<s:
            total+=capacity[ans]
            ans+=1
        return ans