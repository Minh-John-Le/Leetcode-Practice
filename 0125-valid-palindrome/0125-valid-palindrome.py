class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left = 0
        right = len(s) - 1  

        while right > left:
            if not s[right].isalpha() and not s[right].isdigit(): 
                right -= 1
                continue
            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
                continue

            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        return True