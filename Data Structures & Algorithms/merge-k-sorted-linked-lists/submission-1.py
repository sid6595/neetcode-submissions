# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# input list of individual sorted linked lists
# output a singular sorted linked list

# key info
# the input linked lists are sorted already
# can we have negative numbers -> yes

# examples
# [[1,2], [3]] -> [1,2,3]
# [] -> []
# [[]] -> []
# [[4,5,6], [1,2]] -> [1,2,4,5,6]
# [[1,3,7], [4,5,6], [2]]

# approach
# list of list nodes, minimums
# look at each of our starting nodes
# go through all our list nodes (initial)


class NodeComp:

    def __init__ (self, node):
        self.node = node
    
    def __lt__(self, othernode):
        return self.node.val <= othernode.node.val

class Solution:    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        dummy = ListNode(0)
        cur = dummy

        heap = []

        for l in lists:
            if l is not None:
                heapq.heappush(heap, NodeComp(l))

        while heap:
            nodecomp = heapq.heappop(heap)
            actual_node = nodecomp.node
            
            if actual_node.next:
                heapq.heappush(heap, NodeComp(actual_node.next))
                
            cur.next = actual_node
            cur = actual_node
        
        return dummy.next

        