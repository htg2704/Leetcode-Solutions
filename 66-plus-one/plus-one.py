class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        if a[-1]!=9:
            a[-1]+=1
            return a
        i = len(a)-1
        while(i>=0):
            if(a[i]!=9):
                a[i]+=1
                return a
            else:
                a[i]=0
            i-=1
        return [1]+a
        