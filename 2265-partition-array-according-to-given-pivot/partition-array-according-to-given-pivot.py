class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        big = []
        count = 0
        for i in nums:
            if i <pivot:
                small.append(i)
            elif i>pivot:
                big.append(i)
            else:
                count+=1
        small += [pivot]*count
        small += big
        return small