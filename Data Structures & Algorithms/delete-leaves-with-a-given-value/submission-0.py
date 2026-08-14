# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node, prev_node, side):
            # recurse down

            if node.left:
                dfs(node.left, node, "left")
            if node.right:
                dfs(node.right, node, "right")
            if not node.left and not node.right:
                if node.val == target:
                    if side == "left":
                        prev_node.left = None
                    elif side == "right":
                        prev_node.right = None
                    else:
                        return None
            
            return node

        
        return dfs(root, None, "")


        