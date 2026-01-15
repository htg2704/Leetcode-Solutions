class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hb: List[int], vb: List[int]) -> int:
        hb.sort()
        vb.sort()
        cur = 1
        mxh, mxv = 1,1
        for i in range(1,len(hb)):
            if hb[i]-hb[i-1]==1:
                cur+=1
            else:
                cur=1
            mxh=max(cur,mxh)
        mxh+=1
        cur=1
        for i in range(1,len(vb)):
            if vb[i]-vb[i-1]==1:
                cur+=1
            else:
                cur=1
            mxv=max(cur,mxv)
        mxv+=1
        return min(mxh,mxv)**2
        