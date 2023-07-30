class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        carGroup = []
        for i in range(0, len(position)):
            carGroup.append([position[i], speed[i]])
        
        carGroup = sorted(carGroup, key=lambda tup: tup[0])

        stack = []
        for p,s in carGroup[::-1]:
            time = (float)(target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
                
                
        