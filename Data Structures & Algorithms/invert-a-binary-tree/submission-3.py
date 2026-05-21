# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# goal: swap left and right nodes

# given root
# invert binary tree
# recursively swap left and right for all subtrees

# return new root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        curLeft = root.left
        curRight = root.right

        root.left = curRight
        root.right = curLeft

        return root


        