class FirstAndLastElemen {
    public int[] searchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        if (nums.length == 0)
        {
            return new int[] {-1 , -1};
        }
        
        if (nums.length == 1 && nums[0] == target)
        {
            return new int[] {0 , 0};
        }
        
        while (right > left)
        {
            int mid = left + (right - left) / 2;
            
            if( nums[mid] > target)
            {
                right = mid - 1;
            }
            else if (nums[mid] == target)
            {
                left = mid;
                right = mid;
                break;
            }
            else
            {
                left = mid + 1;
            }
            
        }
        
        while (right >= 0 && right < nums.length && nums[right] <= target)
        {
            right++;
        }
        
        while (left >= 0 && nums[left] >= target)
        {
            left--;
        }
        
        if(left + 1 > right - 1)
        {
            return new int[] {-1,-1};
        }
        
        return new int[] {left + 1, right - 1};
        
    }
}

/*
this is binary Search 

runtime = O(logn) + k where n is the size of array 
k is the the range between first and second appearance;



*/
