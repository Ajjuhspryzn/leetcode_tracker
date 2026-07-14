// Last updated: 7/14/2026, 3:20:52 PM
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
    public ListNode mergeTwoLists(ListNode List1, ListNode List2) {
        ListNode dummy=new ListNode();
        ListNode curr=dummy;
        while(List1 !=null && List2 !=null){
            if(List1.val>List2.val){
                curr.next=List2;
                List2=List2.next;
            }else{
                curr.next=List1;
                List1=List1.next;
            }
            curr=curr.next;
        }
        curr.next=(List1 !=null)?List1:List2;
        return dummy.next;
    }
}