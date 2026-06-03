class Solution:
    def isValid(self, s: str) -> bool:
        L=[]
        for x in s:
            if(x=="(" or x=="{" or x=="["):
                L.append(x)
            else:
                if not L:
                    return False
                cur = L.pop()
                if((cur=='(' and x!=")") or (cur=='{' and x!="}") or (cur=='[' and x!="]")):
                    return False
        if L:
            return False
        return True