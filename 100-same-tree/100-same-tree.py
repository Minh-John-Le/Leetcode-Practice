# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pointer = 0;
        queue1 = []
        queue2 = []
        
        queue1.append(p)
        queue2.append(q)
        
        if q is None and p is None:
            return True
        elif (q is None and p is not None) or (q is not None and p is None):
            return False
        
        while(True):      
            p = queue1[pointer]
            q = queue2[pointer]
            if(p.val != q.val):
                return False
            
            if p.left is not None and q.left is not None:
                queue1.append(p.left)
                queue2.append(q.left)
            elif not (p.left is None and q.left is None):
                return False
             
            if p.right is not None and q.right is not None:
                queue1.append(p.right)
                queue2.append(q.right)
            elif not(p.right is None and q.right is None):
                print("her2")
                return False
            
            pointer += 1
            if(pointer == len(queue1)  or pointer == len(queue2)):
                break;
                
            
        return queue1[pointer - 1].val == queue2[pointer - 1].val
       
        