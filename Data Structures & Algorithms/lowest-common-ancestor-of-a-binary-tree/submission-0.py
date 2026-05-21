# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        # will be none if both targets aren't found
        left = self.lowestCommonAncestor(root.left, p, q)

        # will be none if both targets aren't found
        right = self.lowestCommonAncestor(root.right, p, q)

        # found in both subtrees, this is the lca
        if left and right:
            return root
        
        # if we only find in one subtree return that one
        return left if left else right
        