class Solution:
    def findContentChildren(self, Student: List[int], Cookie: List[int]) -> int:
        n, m = len(Student), len(Cookie)
        l, r = 0,0
        Student.sort()
        Cookie.sort()
        while(l<n and r<m):
            if Cookie[r]>=Student[l]:
                l+=1
            r+=1
        return l