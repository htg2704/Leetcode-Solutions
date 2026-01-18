class Solution:
    def isHappy(self, n: int) -> bool:
        def sqsum(num):
            ans = 0
            while num>0:
                x=num%10
                ans+=(x*x)
                num=num//10
            return ans
        if n==1:
            return True
        n1 = sqsum(n)
        n2 = sqsum(sqsum(n))
        while(n1!=n2):
            n1=sqsum(n1)
            n2=sqsum(sqsum(n2))
            if(n1==1 or n2==1):
                return True
        return n1==1