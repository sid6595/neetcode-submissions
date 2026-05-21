# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-inf")
        
        def dfs(node):
            if not node:
                return 0
            # run dfs on left and right branches
            left_path = max(dfs(node.left), 0)
            right_path = max(dfs(node.right), 0)

            # update global max where this node is the pivot
            self.result = max(self.result, left_path + right_path + node.val)

            # return the best value this node can provide
            return max(left_path, right_path) + node.val
        
        dfs(root)
        return self.result
        