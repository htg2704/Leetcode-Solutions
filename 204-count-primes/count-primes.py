class Solution:
    def countPrimes(self, n: int) -> int:
        isprime = [True]*(n+1)
        ans = []
        for i in range(2, n+1):
            if isprime[i]:
                ans.append(i)
                for j in range(i*i, n+1, i):
                    isprime[j]=False
        num = 0
        for i in ans:
            if i<n:
                num+=1
        return num
