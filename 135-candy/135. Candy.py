class Solution:
    def candy(self, arr: List[int]) -> int:
        n=len(arr)
        a = [1]*n
        for i in range(1,n):
            if(arr[i]>arr[i-1]):
                a[i]=a[i-1]+1
        for i in range(n-2,-1,-1):
            if(arr[i]>arr[i+1] and a[i]<a[i+1]+1):
                a[i]=a[i+1]+1
        print(a)
        return sum(a)

        