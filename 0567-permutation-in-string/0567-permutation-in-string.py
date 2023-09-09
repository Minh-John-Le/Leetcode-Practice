class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # make dict of char count in s1 
        s1Dict = [0] * 26
        for char in s1:
            s1Dict[ord(char) - ord('a')] += 1
            
        left = 0
        for i in range(0, len(s2)):
            pos = ord(s2[i]) - ord('a')

            s1Dict[pos] -= 1

            if s1Dict[pos] < 0:
                while left <= i:
                    pos2 = ord(s2[left]) - ord('a')
                    s1Dict[pos2] += 1
                    left += 1 

                    if pos2 == pos:
                        break
            else: 
                if len(s1) == (i - left + 1):
                    return True
        
        return False
 