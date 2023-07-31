class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (bottom - top) // 2 + top
            
            if matrix[mid][0] <= target and matrix[mid][len(matrix[0]) - 1] >= target:
                # Search by row
                left = 0
                right = len(matrix[0]) - 1
                row = mid
                print("here")
                
                while left <= right:
                    mid = (right - left) // 2 + left

                    if matrix[row][mid] == target:
                        return True

                    if  matrix[row][mid] < target:
                        left = mid + 1
                    elif matrix[row][mid] > target:
                        right = mid - 1
                return False

            if matrix[mid][0] < target:
                top = mid + 1
            elif matrix[mid] > target:
                bottom = mid - 1

        return False

