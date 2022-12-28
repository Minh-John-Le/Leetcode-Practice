class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            prefix = strs[0] 
        
        for word in strs:
            count = 0
            
            # early termination if find a non match
            if prefix == "":
                return prefix

            # Go through each char in the word, and update current prefix
            for char in word:
                # index out of bound check
                if count >= len(word) or count >= len(prefix):
                    break

                # termination when the prefix character not in the word
                if char != prefix[count]:
                    break
                count += 1

            # update prefix
            prefix = word[0:count]
        return prefix

'''
Run time is O(n) since we iterate through the string array once
Space is about length of longest word since we might store it as the prefix
'''
            
        
        
        