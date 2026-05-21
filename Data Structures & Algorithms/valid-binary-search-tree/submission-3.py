# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given: binary search tree -> node
# output: is this tree a binary search tree -> bool

# key info
# bst: left subtree is less than node's val, right subtree is greater
# doesnt have to be a complete tree

# examples
# [] -> true
# [2,1,3] -> true
# [1,2,3] -> false

# BFS -> level by level
# inorder traversal
# make sure left child is less than parent, right child is greater
# keep adding to queue as long as children exist
# stop once the queue is empty

#       4
#.  1.      8
#         6    9
#        5    7  10

# at each node, store whether its a left or right and the parent value
# if right child
#.   left grandchild: <right child, >grandparent
#    right grandchil: >right child, >grandparent

# if left child
#.   left grandchild
#    right grandchild

# TC: O(n * m)
# SC: O(n * m)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque()
        queue.append((root, -1001, 1001))

        while queue:
            node, min_val, max_val = queue.popleft()

            if node.left:
                if node.left.val < node.val and min_val < node.left.val < max_val:
                # fix append
                    queue.append((node.left, min_val, node.val))
                else:
                    return False
            
            if node.right:
                if node.right.val > node.val and min_val < node.right.val < max_val:
                # fix append
                    queue.append((node.right, node.val, max_val))
                else:
                    return False
        
        return True
        