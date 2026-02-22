class Solution:
    def binaryGap(self, n: int) -> int:
        bi = bin(n)[2:]
        if bi.count('1')<2:
            return 0
        i,j = 0,1
        ans=0
        while(j<len(bi)):
            #print(bi[i], bi[j])
            if(bi[i]=='1' and bi[j]=='1'):
                ans=max(ans, j-i)
                i+=1
                j+=1
            elif(bi[i]=='1'):
                j+=1
            elif(bi[j]=='1'):
                i+=1
            else:
                i+=1
                j+=1

        return ans
        