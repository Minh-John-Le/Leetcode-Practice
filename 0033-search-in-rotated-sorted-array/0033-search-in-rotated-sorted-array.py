class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # use binary search to find start location
        start = 0

        if nums[0] > nums[-1]:
            start = len(nums) - 1
            end = 0

            while True:
                mid = (start + end) // 2
                if mid == end:
                    break
                
                if nums[mid] > nums[end]:
                    end = mid
                else:
                    start = mid
        
        left = -1
        right = -1
        if target <= nums[-1]:
            left = start
            right = len(nums) - 1
        else:
            left = 0
            right = start - 1

        # Binary search after find the start number location
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
        