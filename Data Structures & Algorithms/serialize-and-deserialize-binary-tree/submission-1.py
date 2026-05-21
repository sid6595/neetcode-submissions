# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# convert a binary tree into a string
# convert that string back into a tree

# each node has 3 components: value, 2 children

# we need a separator for each, let's use '!'
# example: serialize
# [1,2,3] -> 1!2!3!
# [1,null,3] -> 1!@!3!

# deserialize
# 1!2!3! -> [1, 2, 3]
# 1!@!3! -> [1, null, 3]

class Codec:
    separator = '!'
    no_child = '@'
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '@'
        
        result = []

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            
            if not node:
                result.append("@")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return "!".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split('!')
        if vals[0] == "@":
            return None

        root = TreeNode(int(vals[0]))
        queue = deque()
        queue.append(root)
        index = 1

        while queue:
            node = queue.popleft()
            if vals[index] != "@":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            if vals[index] != "@":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root
                


