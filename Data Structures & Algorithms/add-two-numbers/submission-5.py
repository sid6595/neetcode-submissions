# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# if the numbers are passed in reverse order we can do normal addition
# when we need to carry the 1, store it for the next set of elements

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        home = ListNode(0)

        start_a = l1
        start_b = l2
        carry = 0

        cur = home

        while start_a or start_b or carry:
            # get values
            # what if start_a or start_b doesn't exist; i.e. - different lengths

            val_a = start_a.val if start_a else 0
            val_b = start_b.val if start_b else 0

            sum_here = val_a + val_b + carry
            digit = sum_here % 10
            if sum_here >= 10:
                carry = 1
            else:
                carry = 0
            
            cur.next = ListNode(digit)
            temp = cur.next
            cur = temp

            if start_a:
                start_a = start_a.next
            if start_b:
                start_b = start_b.next
        
        return home.next

        