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
class RemoveDuplicateII {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null)
        {
            return head;
        }
        ListNode dummyHead = new ListNode(7);
        ListNode solution = dummyHead;
        ListNode previousNode = head;
        ListNode currentNode = head;
        
        
        while (currentNode.next != null)
        {
            previousNode = currentNode;
            currentNode = currentNode.next;
            
            if(currentNode.val != previousNode.val) // add node to the solution if it is not repeat
            {
                dummyHead.next = previousNode;
                dummyHead = dummyHead.next;
                
            }
            else
            {
                // get rid of all duplicate node
                while (currentNode.val == previousNode.val && currentNode.next != null)
                {
                    previousNode = currentNode;
                    currentNode = currentNode.next;
                }
            }
            
            
        }
        
        if (previousNode.val != currentNode.val)
        {
            dummyHead.next = currentNode;
        }
        else
        {
            dummyHead.next = null;
        }
        
        return solution.next;
    }
    
}

/*
Idea have two pointer
Pointer1 control the current index of returning array.
Pointer2 iterate thorugh array

Run-time
O(n) since we iterate through array once



*/
