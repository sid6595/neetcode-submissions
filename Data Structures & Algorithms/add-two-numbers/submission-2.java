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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        //create new linked list (answer)
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carryOver = 0;
        //while one of the two are not empty
        while(l1 != null || l2 != null){
            int sum = carryOver;
            carryOver = 0;
            if(l1 != null){
                sum = sum + l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                sum = sum + l2.val;
                l2 = l2.next;
            }
            if(sum >= 10){
                sum = sum % 10;
                ListNode node = new ListNode(sum);
                current.next = node; 
                current = current.next;
                carryOver = 1;
            }
            else{
                ListNode node = new ListNode(sum);
                current.next = node; 
                current = current.next;
            }
        }
        if(carryOver > 0){
            current.next = new ListNode(carryOver);
        }
        return dummy.next;
    }
}
