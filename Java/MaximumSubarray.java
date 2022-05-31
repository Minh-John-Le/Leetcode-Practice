class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        
        
        int max = nums[0];
        int prevMax = nums[0];
        
        for (int i = 1; i < nums.length; i++)
        {
            prevMax = Math.max(nums[i], nums[i] + prevMax);
            max = Math.max(max, prevMax);
        }
     
        return max;
    
    }
}

/*
Idea use dynamic programing:
since this is overlapping problem. Also it aks for the largest sum

Runtime O(n) since iterate thorugh array once



*/
