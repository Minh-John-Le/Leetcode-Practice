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
class AddTwoNumber {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sumVal = 0;
        
        ListNode result = new ListNode();
        ListNode cuurentNode = result;
    
        while (l1 != null || l2 != null )
        {
            if (l1 == null)
            {
                sumVal = (int)(sumVal / 10) + l2.val;
                l2 = l2.next;
            }
            else if (l2 == null)
            {
                sumVal = (int)(sumVal / 10) + l1.val;
                l1 = l1.next;
            }
            else
            {
               sumVal = (int)(sumVal / 10) + l1.val + l2.val;
                l1 = l1.next;
                l2 = l2.next;
            }
            
            
            cuurentNode.next = new ListNode();
            cuurentNode = cuurentNode.next;
            cuurentNode.val = sumVal % 10;
        }
        
        if((int)(sumVal / 10) > 0)
        {
            cuurentNode.next = new ListNode(1);
        }

            
        return result.next;
    }
}

/*
Time complexity = O(m+n)

*/
