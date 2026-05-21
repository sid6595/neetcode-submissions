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
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        while(slow != null){
            Set<ListNode> visited = new HashSet<>();
            visited.add(slow);
            ListNode fast = slow.next;
            while(fast != null){
                if(visited.contains(fast)){
                    return true;
                }
                visited.add(fast);
                fast = fast.next;
            }
            slow = slow.next;
        }
        return false;
    }
}
