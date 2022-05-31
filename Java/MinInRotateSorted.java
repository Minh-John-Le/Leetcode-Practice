class MinInRotateSorted {
    public int findMin(int[] nums) {
        int pointer1 = 0;
        int pointer2 = nums.length - 1;
        
  
        while (pointer1 < pointer2 && nums[pointer1] >= nums[pointer2])
        {
            int mid = pointer1 + (pointer2 - pointer1) / 2;
          
            
            if (nums[mid] >= nums[pointer1])
            {
                pointer1 = mid + 1;
       
            }
            else
            {
                pointer2 = mid;
            }
        }
        
        pointer1 = Math.min(pointer1, nums.length - 1);
       
        return Math.min(nums[pointer1], nums[pointer2]);
        
    }
}


/*
Idea use binary search to determine the postion of smallest number 

--> the rotation number
run-time = O(logn)



*/
