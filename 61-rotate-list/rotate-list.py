# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t = head
        if(head is None):
            return None
        l = 1
        while(t.next):
            l+=1
            t = t.next
        
        t.next = head
        k = k%l
        x = l-k
        te = head
        for i in range(x-1):
            te = te.next
        ans = te.next
        te.next = None
        return ans