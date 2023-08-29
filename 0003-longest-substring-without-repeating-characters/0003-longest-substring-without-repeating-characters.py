class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        longest = 0

        while True:
            if right >= len(s):
                return longest 

            while left < right and s[right] in s[left:right]:
                left += 1

            longest = max(longest, right - left + 1)
            right += 1
                