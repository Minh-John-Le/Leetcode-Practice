# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        queueLeft = []
        queueRight = []

        # get the left and right branch
        queueLeft.append(root.left)
        queueRight.append(root.right)

        # for each itteration we will compare the left of left branch with the right of right brach. Then the oposite the right of left branch with the left of right branch
        while queueLeft and queueRight:
            currentLeft = queueLeft.pop()
            currentRight = queueRight.pop()
               
            if currentLeft == None and currentRight == None:
                continue

            # check if one brach is terminate 
            if currentLeft == None or currentRight == None:
                return False

            # compare their value
            if currentLeft.val != currentRight.val:
                return False
            
            # add their children node to the queue
            else:
                queueLeft.append(currentLeft.left)
                queueLeft.append(currentLeft.right)

                queueRight.append(currentRight.right)
                queueRight.append(currentRight.left)

        return True

    """
    Runtime is O(n) since we iterrate through the whole tree once 
    Space is O(n) since we store at max the number of node in the tree
    """