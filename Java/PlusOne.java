
public class PlusOne {
	public static void main(String[] args)
	{
		SolutionPlusOne solution = new SolutionPlusOne();
		int[] s = {9};
		int[] a = solution.plusOne(s);
		for(int i = 0; i < a.length; i++)
		{
			System.out.println(a[i]);
		
		}
		
	}

	
}

class SolutionPlusOne {
	public int[] plusOne(int[] digits) {
        int currentIndex = digits.length - 1;
        int memmory = 0; //this hold one digit from current number
        while(currentIndex >= 0 
        		&& memmory == 0) // continue the plus if last digit were 10
        {
        	digits[currentIndex]++; // add one to the current digit
        	memmory = (int)(digits[currentIndex] % 10); // get one digit
        	digits[currentIndex] = memmory; // set that digit to current digit
        	currentIndex--; // go to next digit
        }
        
        if(digits[0] == 0) // create a new array when we have extra digit in front 
        {
        	int[] newdigits = new int[digits.length + 1];
        	newdigits[0] = 1;
        	for(int i = 0; i < digits.length; i++)
        	{
        		newdigits[i+1] = digits[i];
        	}
        	return newdigits;
        }
        
        return digits;
	
        
    }
}