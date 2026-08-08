# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# has to be strictly greater than x, equal is fine
# we need to traverse the whole tree, see every node
# need to know the path to each node
# DFS

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(n, max_seen):
            if not n:
                return
            if n.val >= max_seen:
                self.res += 1
                max_seen = n.val
            dfs(n.left, max_seen)
            dfs(n.right, max_seen)

        
        dfs(root, float('-inf'))
        return self.res


        