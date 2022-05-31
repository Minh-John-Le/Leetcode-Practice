class HouseRobber {
    
    public int rob(int[] nums) {
        int[] money = new int[nums.length];
        money[0] = nums[0];
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer> (Comparator.reverseOrder());
        maxHeap.add(0);
        
        for (int i = 1; i < nums.length; i ++)
        {
            money[i] = maxHeap.peek() + nums[i];
            maxHeap.add(money[i - 1]);
        }
        maxHeap.add(money[nums.length - 1]);
        return maxHeap.peek();

    }
}

/*
This is a part of dynamic program where we record the previous tacking money;
run time
n iterartion through the array
logn add integer to max heap
--> O(nlogn)

*/
