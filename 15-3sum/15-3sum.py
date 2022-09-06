class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        print(nums)
        result = []
        dictionary = dict()
        for cIndex in range(0, len(nums) - 2):
            c = nums[cIndex]
            
            aIndex = cIndex + 1
            bIndex = len(nums) - 1
            while(aIndex <= bIndex):
                if(nums[aIndex] + nums[bIndex] + c == 0) and (aIndex != bIndex):
                    if (nums[cIndex] not in dictionary):
                        dictionary[nums[cIndex]] = [nums[aIndex]]
                    else:
                        if nums[aIndex] not in dictionary[nums[cIndex]]:
                            dictionary[nums[cIndex]].append(nums[aIndex])
                    aIndex += 1
                    bIndex -= 1
                elif(nums[aIndex] + nums[bIndex] + c > 0):
                    bIndex -= 1
                else:
                    aIndex += 1
         
        for key in dictionary:
            for item in dictionary[key]:
                result.append([key,item, - key - item])
        return result
                     
                    
                    
                
        