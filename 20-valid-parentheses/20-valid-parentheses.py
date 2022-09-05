class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        glossal = {"{":"}",  "[":"]", "(":")"}
        
        stack = ['0']
        s = s + '0'
        for char in s:
            if char in glossal:
                stack.append(glossal[char])
            else:
                if(stack.pop() != char):
                    return False
                
        return True