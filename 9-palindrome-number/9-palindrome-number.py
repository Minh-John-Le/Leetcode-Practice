class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        
        power = len(str(x)) - 1
        
        while(x > 0):
            
            largestPlace = x / (10**power)  
            decimalPlace = x % 10

            if(largestPlace != decimalPlace):
               return False
            x  = x - largestPlace * (10**power)
            x  = x / 10
            power -= 2;
            
        return True    
            
            