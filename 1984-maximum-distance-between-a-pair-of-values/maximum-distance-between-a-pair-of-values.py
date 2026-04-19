class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxd = 0
        l1,l2 = 0,0
        n1,n2 = len(nums1), len(nums2)
        while(l1<n1 and l2<n2):
            if(nums1[l1]<=nums2[l2] and l1<=l2):
                maxd=max(maxd, l2-l1)
                l2+=1
            elif(l1<=l2):
                l1+=1
            else:
                l2+=1
        return maxd

        