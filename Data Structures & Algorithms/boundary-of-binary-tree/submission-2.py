# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# output order 
# root + left boundary + leaves left to right + right boundary

# left/right boundary
# left child, left child of left boundary, if no left child in left boundary -> right child
# leaf nodes do not count, root node does not count

# questions
# are the boundaries essentially each node you can see from the left or right not including the root and leaves
# are all inputs valid? 
# how big can the tree be?
# will the tree be balanced?
# does the order of the boundary nodes matter? 

class Solution:
    def getBoundary(self, node, side):
        
        if side == 'left':
            if node.left:
                return [node.val] + self.getBoundary(node.left, 'left')
            elif node.right:
                return [node.val] + self.getBoundary(node.right, 'left')
            else:
                return []
        if side == 'right':
            if node.right:
                return self.getBoundary(node.right, 'right') + [node.val]
            elif node.left:
                return self.getBoundary(node.left, 'right') + [node.val]
            else:
                return []

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        left_boundary = []
        if root.left:
            left_boundary = self.getBoundary(root.left, 'left')
        right_boundary = []
        if root.right:
            right_boundary = self.getBoundary(root.right, 'right')
        if not root.left and not root.right:
            return [root.val]
        
        

        def dfs(node):
            res = []
            if not node:
                return []
            
            if node.left:
                res += dfs(node.left)
            if node.right:
                res += dfs(node.right)
            if not node.left and not node.right:
                res.append(node.val)
            
            return res
            
        leaves = dfs(root)
        print(root.val, left_boundary, leaves, right_boundary)
        return [root.val] + left_boundary + leaves + right_boundary