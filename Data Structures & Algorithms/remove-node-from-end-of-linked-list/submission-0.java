/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode holder = head;
        ListNode start = head;
        int numNodes = 0;
        while(start != null){
            numNodes++;
            start = start.next;
        }

        if (n == numNodes) {
            return head.next;
        }

        int indexToRemove = numNodes - n;
        ListNode current = head; 
        ListNode prev = null;
        int counter = 0;
        while(current != null){
            if(counter == indexToRemove){
                prev.next = current.next;
                break; 
            }
            prev = current; 
            current = current.next;
            counter++;
        }
        return holder;
    }
}
