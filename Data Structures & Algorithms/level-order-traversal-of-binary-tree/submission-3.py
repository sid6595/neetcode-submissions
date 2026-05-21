# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs
# level by level
# append to result list

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return []

        stack = deque()
        stack.append(root)

        while stack:
            sublist = []
            for i in range(len(stack)):
                current = stack.popleft()
                sublist.append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
            result.append(sublist)
        
        return result


        