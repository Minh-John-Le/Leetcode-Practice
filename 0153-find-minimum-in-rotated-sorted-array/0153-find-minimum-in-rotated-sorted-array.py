class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] > nums[-1]:
            left = len(nums) - 1
            right = 0
        else:
            return nums[0]

        while True:
            mid = abs(right - left) // 2 + min(left, right)
    
            if mid == right:
                return nums[left]
            
            if nums[mid] > nums[right]:
                right = mid
            else:
                left = mid
        