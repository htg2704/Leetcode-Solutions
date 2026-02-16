class Solution:
    def reverseBits(self, n: int) -> int:
        bins = bin(n)[2:].zfill(32)
        return int(bins[::-1], 2)
        