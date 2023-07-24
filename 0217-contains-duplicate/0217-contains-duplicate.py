class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) <= 1:
            return False
         
        numSorted = sorted(nums)
        currentNum = numSorted[0]
        
        for i in range(1, len(numSorted)):
            if currentNum == numSorted[i]: 
                return True
            currentNum = numSorted[i]
        return False