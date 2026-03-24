# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent={}
        q=deque()
        q.append(root)
        while(q):
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    parent[node.left.val]=node
                    q.append(node.left)
                if node.right:
                    parent[node.right.val]=node
                    q.append(node.right)
        vis = {}
        q.append(target)
        while(k>0 and q):
            n = len(q)
            for _ in range(n):
                node=q.popleft()
                vis[node.val]=1
                if node.left and node.left.val not in vis:
                    q.append(node.left)
                if node.right and node.right.val not in vis:
                    q.append(node.right)
                if node.val in parent and parent[node.val].val not in vis:
                    q.append(parent[node.val])
            k-=1
        while(q):
            ans.append(q.popleft().val)
        return ans
                
        