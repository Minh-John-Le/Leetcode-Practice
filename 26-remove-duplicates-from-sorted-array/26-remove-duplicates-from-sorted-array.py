class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pointer = 0
        
        for num in nums:
            if num > nums[pointer]:               
                pointer +=1

                nums[pointer] = num
        return pointer + 1        
    
        