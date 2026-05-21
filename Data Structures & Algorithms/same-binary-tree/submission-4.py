# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# traverse each node, if they're not equal return false

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False

        if self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left):
            return p.val == q.val
        else:
            return False
        

        