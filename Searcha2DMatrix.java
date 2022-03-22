class Solution {
    public boolean Searcha2DMatrix(int[][] matrix, int target) {
        
        int index = 0;
        int row = matrix.length - 1;
        int col = matrix[0].length - 1;
        
        
        // this to get into correct row
        while (index <= row)
        {
            int mid = index + (row - index) / 2;
            
            if (matrix[mid][0] < target)
            {
                index = mid + 1;
            }
            else if (matrix[mid][0] == target)
            {
                return true;
            }
            else
            {
                row = mid - 1;
            }
        }
        
        if( matrix[Math.min(index, matrix.length - 1)][0] < target)
        {
            row = Math.min(index, matrix.length - 1);
        }
        else
        {
            row = Math.max(row, 0);
        }
        

        
        // Get to correct collumn
        index = 0; 
        while (index <= col)
        {
            int mid = index + (col - index) / 2;
            
            if (matrix[row][mid] < target)
            {
                index = mid + 1;
            }
            else if (matrix[row][mid] == target)
            {
                return true;
            }
            else
            {
                col = mid - 1;
            }
        }
        
        
        
        return false;
    }
}


/*
  Idead:
  This is a matrix  with property of increase in both collumn and row
  So to idenity a pair(row and collum) 
  , I will do 2 direction binary search
  
    runtime: 2*O(lgn) = O(lgn)
*/
