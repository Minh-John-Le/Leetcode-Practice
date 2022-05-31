class ClimbingStairs {
    private int[] stepSolution = new int[46];// posible solution
    public int climbStairs(int n) {
        stepSolution[1] =  1;
        stepSolution[2] =  2;
        
        for(int i =  3; i <= n; i++)
        {
            stepSolution[i] = stepSolution[i - 1] + stepSolution[i - 2] ;
        }
        return stepSolution[n];
        
    }
    
}

/*
I will try Dynamic program
we find how many solution for 1 steps and record it then 2 steps and records it
3 steps could be 1 step + 2 steps but we already how many solution for each. Thus we just need multiply those two

runtime - O(n) since we calculate from 1--> n steps

*/
