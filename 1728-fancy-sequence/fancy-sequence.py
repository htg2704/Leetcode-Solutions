class Fancy:
    mod = 10**9 + 7

    def __init__(self):
        self.arr = []
        self.s = 0
        self.m = 1

    def append(self, val: int) -> None:
        val = (val - self.s) % self.mod
        val = val * pow(self.m, self.mod - 2, self.mod) % self.mod
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.s = (self.s + inc) % self.mod

    def multAll(self, mul: int) -> None:
        self.m = (self.m * mul) % self.mod
        self.s = (self.s * mul) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.m + self.s) % self.mod
