class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def countone(i):
            b = bin(i)[2:]
            return b.count('1')
        prime = [2,3,5,7,11,13,17,19]
        primes=set(prime)
        ans=0
        for j in range(left, right+1):
            #print(countone(j))
            if(countone(j) in primes):
                ans+=1
        return ans

        