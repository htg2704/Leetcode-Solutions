class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        def subs(s, k):
            se = set()
            for i in range(len(s)-k+1):
                if s[i:i+k] in se:
                    continue
                else:
                    se.add(s[i:i+k])
            #print(se)
            return len(se)
        return (subs(s, k)==2**k)
        