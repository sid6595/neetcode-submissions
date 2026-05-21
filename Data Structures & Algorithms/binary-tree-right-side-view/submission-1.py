# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given root
# only return right nodes

# approach 1
# start at root node
# go down every right child
# if at any point, there is no right child, choose the left child

# approach 2
# level by level BFS approach
# a queue of all the nodes we've traveled
# within each level, add each node to a stack
# once i reach the end of the level, pop the last element in the stack and add to result and reset 
# return our result

# TC: O(n)
# SC: [queue] O(n) + [stack] O(n) = O(n)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = []

        if root:
            queue.append(root)
        
        """
        [1]
        []
        [2, 3]
        [3]
        [3, 4]
        [4]
        [4,5]
        [5]
        []
        """
        while queue:
            seen = []
            for i in range(len(queue)):
                current = queue.popleft()
                seen.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(seen[-1])
        
        return result
            

        