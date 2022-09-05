# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        
        while(head != None):
            stack.append(head.val)
            head = head.next
        pointer1 = 0;
        pointer2 = len(stack) - 1;
        
        while(pointer1 < pointer2):
            if(stack[pointer1] != stack[pointer2]):
                return False
            pointer1 += 1
            pointer2 -= 1
        return True    