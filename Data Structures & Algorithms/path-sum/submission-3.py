# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 

# input: binary tree, integer -> targetSum
# output: boolean -> true if a root-leaf path exists with values summing to targetSum

# additional info
# complete binary tree? - not necessarily
# can we see empty tree/ no input? - yes
# can we have negative numbers? - yes

# examples
# [1,2,3] -> true

# backtracking algo
# each node
# check if node is valid
# check if it's a leaf node -> if yes, check if equal to sum
# if no -> check the left subtree for solution then the right
# return false at the end

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helperPathSum(root, currentSum):
            if not root:
                return False
            
            currentSum += root.val
            
            if not root.right and not root.left:
                return currentSum == targetSum
            
            if helperPathSum(root.left, currentSum):
                return True
            if helperPathSum(root.right, currentSum):
                return True
            

            return False
        
        return helperPathSum(root, 0)
        