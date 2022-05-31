class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> solution = new HashMap<Integer, Integer>();  
        
        for (int i = 0; i < nums.length; i++)
        {
            if(!solution.containsKey(nums[i]))
            {
                solution.put(nums[i], i);
            }
            else 
            {
               return true;
            }
               
        }
               
        return false;
    }
}

/*
Time-Complexity O(n) since iterate through the array maximum 1
Space-Complexity O(n) max is the number of entry in array that is added to the hasmap

*/
