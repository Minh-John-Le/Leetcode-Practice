class SearchRotateSortedArray {
    public int search(int[] nums, int target) {
        int left = nums.length - 1;
        int right = 0;
        
        
        // this loop will help find the pivot
        while (left - 1 > right)
        {
            int mid = right + (left - right) / 2;
            
            if(nums[right] < nums[mid])
            {
                right = mid;
            }
            else
            {
                left = mid;
            }
        }
        
        // This ensure left is the smallest, while right is the largest
        if(nums[left] >= nums[right])
        {
            left = 0;
            right = nums.length - 1;
        }
        
        
        // check the first sorted part
        if(nums[0] <= target)
        {
            int newLeft = 0;
                
            while (right >= newLeft)
            {
                int mid = newLeft + (right - newLeft);
                
                if (nums[mid] > target)
                {
                    right = mid - 1;
                }
                else if (nums[mid] == target)
                {
                    return mid;
                }
                else
                {
                    newLeft = mid + 1;
                }
                    
            }
        }
        // check the second sorted part
        else
        {
            int newRight = nums.length - 1;
                
            while (newRight >= left)
            {
                int mid = left + (newRight - left);
                
                if (nums[mid] > target)
                {
                    newRight = mid - 1;
                }
                else if (nums[mid] == target)
                {
                    return mid;
                }
                else
                {
                    left = mid + 1;
                }
                    
            }
        }
        
        return -1;
    }
}

/*
Idea use binary Search to find the place of pivot
--> we will have 2 sorted part
binary search through both give use the answer

Runtine 
Find the pivot O(lgn)
Binary search first part O(lg(n - k));/ k is pivot location
Or
Binary search second part O(lg(length - k);
either of them is less than O(lg(n))

--> total is 2*O(lgn) = O(lgn);


*/
