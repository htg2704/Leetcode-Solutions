class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []
        seen = set()
        common = 0
        
        for i in range(n):
            if A[i] not in seen:
                seen.add(A[i])
            elif A[i] in seen:
                common += 1
            if B[i] not in seen:
                seen.add(B[i])
            elif B[i] in seen:
                common += 1
            ans.append(common)
        return ans