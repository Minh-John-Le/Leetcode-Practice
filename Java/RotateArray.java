public class RotateArray {
	public static void main(String[] args)
	{
		int[] a = new int[]{1,2,3,4,5,6,7};
		int k = 3;
		SolutionRotateArray solution = new SolutionRotateArray();
		solution.rotate(a, k);
		
		for (int i = 0; i < a.length; i ++)
		{
			System.out.print(a[i] + ", ");
		}
	}

	
}

class SolutionRotateArray 
{
	public void rotate(int[] nums, int k) {
        while(k > nums.length -1)
        {
            k = k - nums.length;
        }
        
        reverseArray(nums, 0, nums.length - 1);
        reverseArray(nums, 0, k - 1);
        reverseArray(nums, k, nums.length - 1);
    }
    
        
      
    private void reverseArray(int[] nums, int start, int end)
    {
        int temp;
        while(start < end)
        {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            end--;
            start++;
        }
    }
    
    
}

/*
Time-Complexity 
O(n) since we iterate through the array twice
Space Complexity = O(1)



*/