# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: TreeNode
# goal: nested list of traversal, each sublist is a level

# examples
# [1,2,3,4,5] -> [[1], [2,3], [4,5]]
# [1, 2, null, 4, null, null, null] -> [[1], [2], [4]]
# [] -> []

# approach
# BFS
# initialize a queue with the root
# while our queue is populated
# iterate through each level starting from the root
# initialize a sublist, add each node in our level
# append sublist to our result list 
# make sure to keep adding left and right child nodes to queue when they exist

# TC: O(n)
# SC: [queue] O(n) + [list] O(n) = O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        result = []

        queue.append(root)

        while queue:
            sublist = []
            for i in range(len(queue)):
                current = queue.popleft()
                sublist.append(current.val)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(sublist)
        
        return result


        