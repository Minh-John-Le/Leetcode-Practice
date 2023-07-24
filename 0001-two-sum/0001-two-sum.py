class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = dict()
        # key = target - num
        # value num location in nums array

        for i in range(0, len(nums)):
            if nums[i] in numDict.keys():
                return [i, numDict[nums[i]]]
            else:
                numDict[target - nums[i]] = i 
