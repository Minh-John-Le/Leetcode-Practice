# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0,None)
        current = dummy
        carryOn = 0
        nodeVal = 0

        
        while True:
            if not l1 and not l2:
                break

            if l1 and l2:
                newCarryOn = (l1.val + l2.val + carryOn) // 10
                nodeVal = (l1.val + l2.val + carryOn) % 10 
                
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                newCarryOn = (l2.val + carryOn) // 10
                nodeVal = (l2.val + carryOn) % 10 
                l2 = l2.next
            elif not l2:
                newCarryOn = (l1.val + carryOn) // 10
                nodeVal = (l1.val + carryOn) % 10 
                l1 = l1.next

            carryOn = newCarryOn
            current.next = ListNode(nodeVal, None)
            current = current.next

        if carryOn == 1:
            current.next = ListNode(carryOn, None)


        return dummy.next

            
        