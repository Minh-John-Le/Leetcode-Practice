class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left = 0 
        right = len(height) - 1

        # forward check
        for i in range(0, len(height)):
            if height[left] <= height[i]:
                water += min(height[left], height[i]) * (i - left)
                for j in range(left, i):
                    water -= height[j]
                left = i

        # backward check
        for i in range(len(height)-1, left - 1, -1):
            if height[right] <= height[i]:
                water += min(height[right], height[i]) * (right - i)
                for j in range(right, i, -1):
                    water -= height[j]
                right = i


        return water