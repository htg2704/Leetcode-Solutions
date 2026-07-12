# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q=deque()
        q.append(root)
        ans = 0
        while(q):
            node = q.popleft()
            if(node.right is not None):
                q.append(node.right)
            if(node.left is not None):
                q.append(node.left)
            ans = node.val
        return ans
                

        