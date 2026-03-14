class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.ans = ""
        self.solve(0, [k], n, ['a','b','c'],"")
        return self.ans
    
    def solve(self, l,k,n,chars, s):
        if l==n:
            k[0]-=1
            if k[0]==0:
                self.ans = s
            return
        for c in chars:
            if l==0 or s[-1]!=c:
                self.solve(l+1, k, n, chars, s+c)
                if k[0]==0:
                    return
        