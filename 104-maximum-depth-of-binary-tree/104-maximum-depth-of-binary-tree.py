# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
      
        if root == None:
            return 0
        else: 
            currentLevel = []
            currentLevel.append(root)
        
        depth = 0
        # basically we do bread first search to get the depth of the tree
        while True:    
            if len(currentLevel) <= 0:
                return depth

            depth += 1
            
            currentLevel = self.getNextLevelQueue(currentLevel)

            
    # This function will get all Node of next level of the tree except for "None" node
    def getNextLevelQueue(self, currentQueue):
        nextLevelQueue = []
        for node in currentQueue:
            if node.left != None:
                nextLevelQueue.append(node.left)

            if node.right != None:
                nextLevelQueue.append(node.right)
        return nextLevelQueue
            
"""
Run time O(n) since we go through the tree once
Space is O(2^depth) since we need space to store at most all node of the lowest level 
"""