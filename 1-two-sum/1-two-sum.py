class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dictionary = dict();
        for i in range(0, len(nums)):
            val = target - nums[i]
            if val in dictionary.keys():
                return [dictionary[val], i]
            dictionary[nums[i]] = i
        return None
            