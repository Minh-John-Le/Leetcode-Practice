"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        nodeList = []
        res = []
        while head:
            nodeList.append(head)
            res.append(Node(head.val, None, None))
            head = head.next

        res.append(None)
        for i in range(0, len(nodeList)):
            res[i].next = res[i + 1]
            if nodeList[i].random == None:
                res[i].random = None
                continue
            
            res[i].random = res[nodeList.index(nodeList[i].random)]

        return res[0]
            


        