# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: root, subroot
# output: true if subroot exists within root, false otherwise

# cases
# subroot = root -> True
# subroot is empty -> True
# root is empty -> False
# [3] -> True

# keep in mind
# binary tree but not binary search tree

# approach
# helper function: compares 2 nodes to see if they are equal
# search through root tree until we find root of subroot
# then run helper to compare
# if they're the same, return true
# else, resume our tree traversal until we run out of nodes


# TC: [isSubtree] O(n) * [sameTree]


class Solution:   
    def sameTree(self, a, b) -> bool:
        if not a and not b:
            return True
        
        if not a or not b:
            return False
        
        if a.val == b.val:
            return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)
        else:
            return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        status = False
        
        if root.val == subRoot.val:
            status = self.sameTree(root, subRoot)
        if root.left:
            status |= self.isSubtree(root.left, subRoot)
        if root.right:
            status |= self.isSubtree(root.right, subRoot)

        return status

        