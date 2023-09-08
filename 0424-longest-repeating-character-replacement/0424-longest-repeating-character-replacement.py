class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        charCount = [0] * 26
        maxf = 0
        left = 0

        for right in range(0, len(s)):

            charCount[ord(s[right]) - ord('A')] += 1
            maxf = max(maxf, charCount[ord(s[right]) - ord('A')])

            if maxf + k < right - left + 1:
                charCount[ord(s[left]) - ord('A')] -= 1
                left += 1

            

        return len(s) - left

        