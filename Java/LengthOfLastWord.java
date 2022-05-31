public class LengthOfLastWord {
	public static void main(String[] args)
	{
		SolutionLengthOfLastWord solution = new SolutionLengthOfLastWord();
		String s = "a";
		int a = solution.lengthOfLastWord(s);
		System.out.println(a);
		
	}

	
}

class SolutionLengthOfLastWord {
	public int lengthOfLastWord(String s) {
        s = s.trim();
        int count = 0;    
        int currentIndex = s.length() - 1 - count;
            while(currentIndex >= 0 
            	&& !(String.valueOf(s.charAt(currentIndex))).equals(" "))
            {
            	System.out.println((s.charAt(currentIndex)));
            	currentIndex --;
                count++;
            }
            
        return count;
    }
}
