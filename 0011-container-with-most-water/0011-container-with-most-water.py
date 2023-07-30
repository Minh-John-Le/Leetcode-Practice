class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = len(height) - 1
        left = 0
        maxWater = 0;
        
        while(right > left):
            
            maxWater = max(maxWater, min(height[left], height[right]) * (right - left))
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
                

        return maxWater