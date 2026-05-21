# input: root, k
# output: kth smallest value

# key points
# binary search tree
# 1 indexed (0 is not a possible k value)

# examples
# [2, 1, 3] , 1 -> 1
# [] , 4 -> []
# [2, 1, 3] , 4 -> Constraint

# approach
# use the properties of BST to create a sorted array
# take the kth smallest element of that array
# inorder traversal append elements to the array

# TC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []
        
        def traversal(node, k: int):
            if not node or k == 0:
                return k, None

            k, res = traversal(node.left, k)
            if k == 0:
                return k, res
            
            k -= 1
            if k == 0:
                return k, node.val

            return traversal(node.right, k)
        
        _, res = traversal(root, k)
        return res
        

            

            
            
        
        


        