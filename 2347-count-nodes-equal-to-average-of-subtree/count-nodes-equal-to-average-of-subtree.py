# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        c=0
        def rec(node):
            nonlocal c
            if not node:
                return 0,0
            ls, lc = rec(node.left)
            rs, rc = rec(node.right)
            subs = ls+rs+node.val
            subc =lc+rc+1
            if subs//subc == node.val:
                c+=1
            return subs, subc
        rec(root)
        return c
        