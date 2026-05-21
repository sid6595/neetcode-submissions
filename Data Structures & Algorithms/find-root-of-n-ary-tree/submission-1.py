"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # look at each node
        # construct the subtree from that node (looking at the children)
        # create a set of seen values
        # store the seen nodes
        # 

        result = None
        curMax = 0

        seen = set()

        def getHeight(current_node):
            if not current_node:
                return 0
            
            seen.add(current_node.val)

            max_seen = 0

            for child in current_node.children:
                max_seen = max(max_seen, getHeight(child))
            
            return max_seen + 1

        for node in tree:
            if node.val in seen:
                continue
            
            if getHeight(node) > curMax:
                curMax = getHeight(node)
                result = node
        
        return result
            




        