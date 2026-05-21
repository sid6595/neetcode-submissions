# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# binary tree, contains at most 2 children per node
# good node -> path from root to target node contains no nodes with value strictly greater than x

# things to keep in mind
# root node will always a good node

# include the root node as part of comparisons
# 4 -> 1 -> 1 -> 2 ||| 2 is NOT a good node

# approach
# BFS
# look at each layer starting with the root layer
# add the child nodes with the max val seen at that node to our queue -> (TreeNode, int)

# TC: O(n)
# SC: O(n)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        goodNodes = 0

        if root:
            queue.append((root, root.val))
        
        while len(queue) > 0:
            current, maxCurrent = queue.popleft()

            #print(current.val)
            #print(maxCurrent)
            if current.val >= maxCurrent:
                goodNodes += 1
                maxCurrent = current.val
            
            if current.left:
                queue.append((current.left, maxCurrent))
            if current.right:
                queue.append((current.right, maxCurrent))
        
        return goodNodes
        