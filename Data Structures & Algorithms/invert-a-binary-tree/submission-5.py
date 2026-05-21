# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iterative dfs, inorder
# left subtree, root, right subtree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = []
        current = root

        while current or stack:
            # yet to process left subtree
            if current:
                stack.append(current)  
                current = current.left
            # left subtree completed processing
            # 
            else:
                current = stack.pop()
                # we have processed the left side of current
                current.left, current.right = current.right, current.left
                current = current.left

        return root

        

        
        