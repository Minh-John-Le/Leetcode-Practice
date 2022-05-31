class MaximizeNumberofSubsequencesinaString {
    public long maximumSubsequenceCount(String text, String pattern) {
        long pat2 = 0;
        long a = 0;
        long b = 0;
     
        for (int i = text.length() - 1; i >= 0; i--)
        {
            if(text.substring(i, i + 1).equals(pattern.substring(1,2)))
            {
                pat2++;
            }
            
            if(text.substring(i, i + 1).equals(pattern.substring(0,1)))
            {
                   a += pat2;
                   b = b + (pat2 + 1);
            }
        }
        System.out.println(pat2);
        if(pattern.substring(1,2).equals(pattern.substring(0,1)))
        {
            long  c = (long)pat2;
            long d = c * (c + 1) / 2;
            System.out.print(c);
            return d;
        }
        
        return Math.max(a + pat2, b);
    }
        
        
}

/*
Idea : Assume have no other string beside the two that in hte pattern
we can either add first string of pattern in the beginning for max length or 
add the second string in pattern at the end for max string
We compare those two 
in case the patern have similiar string we have 
1 + 2 + 3 + ... n+ + (n + 1) = n * (n + 1) / 2  possible new subsequence

Run time O(n) since we itterate thorugh array Once

Note;
This problem is use long since int have less range than long.




*/
