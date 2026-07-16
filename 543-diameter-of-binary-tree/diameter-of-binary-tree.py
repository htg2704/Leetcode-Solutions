# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def rec(node, dia):
            if node is None:
                return 0
            l, r =rec(node.left, dia),rec(node.right, dia)
            dia[0]=max(dia[0],l+r)
            return 1+max(l,r)

        dia = [0]
        rec(root, dia)
        return dia[0]