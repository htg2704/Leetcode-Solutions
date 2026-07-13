class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a = []
        s = "123456789"
        l = str(low)
        h = str(high)
        for l in range(len(l), len(h)+1):
            for start in range(0,10-l):
                num = int(s[start:start+l])
                if low<=num<=high:
                    a.append(num)
        return a

        