class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        a = arr[:]
        a.sort()
        rank = 1
        for i in a:
            if i not in d:
                d[i]=rank
                rank+=1
        return [d[val] for val in arr]
        