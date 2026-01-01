class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = int("".join(map(str, digits)))
        i+=1
        a = []
        for c in str(i):
            a.append(int(c))
        return a
        