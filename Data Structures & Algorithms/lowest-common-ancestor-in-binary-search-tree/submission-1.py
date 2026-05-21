# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given: root node, node1, node2
# output: node which is the LCA of the 2 nodes

# examples
# [3,4] -> 3
# [None, 5] -> None
# [1, 9] -> 5

# key points
# binary search tree, can use that info when searching through nodes
# ancestor allowed to be descendant of itself
# if p.val > root.val and q.val < root.val -> return root

# approach (DFS)
# check p and q against root node
# if one is greater and one is less or one is equal return the root
# else, they'll both be in one child, recursively call

# TC: O(h) -> O(n)
# SC: O(1)



class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q:
            return None

        # check right subtree
        if(p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        # check left subtree
        elif(p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root




        