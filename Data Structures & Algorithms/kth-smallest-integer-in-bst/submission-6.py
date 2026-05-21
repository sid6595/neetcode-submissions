# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given: bst, k
# output: kth smallest value

# example
# [2, 1, 3] , 1 -> 1

# kth smallest

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        
        def inorder(node):
            # left, node, right
            nonlocal count

            if node.left:
                left = inorder(node.left)
                if left is not None:
                    return left
            
            
            
            count -= 1
            if count == 0:
                return node.val
            
            if node.right:
                return inorder(node.right)
        
        return inorder(root)
        

        